#!/usr/bin/env python3

import datetime
import json
import re
import os
import sys

from substring_matcher.constants import (
    DEFAULT_KEYWORDS_FILE,
    DEFAULT_URLS_FILE,
    VALID_RESPONSES_FOR_NO,
    VALID_RESPONSES_FOR_YES
)
from substring_matcher.trie import Trie, TrieNode
from substring_matcher.trie_builder import TrieBuilder
from substring_matcher.utils.cli_messages import (
    display_confirmation_message_for_keywords,
    display_confirmation_message_for_urls,
    display_farewell_message,
    display_help_tips_for_keyword_input,
    display_help_tips_for_url_input,
    display_incorrect_response_alert,
    display_invalid_keyword_info,
    display_menu_options_for_keyword_source,
    display_menu_options_for_url_source,
    display_options_for_starting_over,
    display_ready_message_for_finding_keywords_in_url,
    display_reminder_for_exiting_the_application,
    display_search_completion_notification,
    display_search_results_summary,
    display_url_keyword_match_data_in_file,
    display_waiting_message_while_building_trie,
    display_warning_to_request_more_keywords,
    display_warning_to_request_more_urls,
    display_waiting_message_during_keyword_matching,
    display_welcome_message
)
from substring_matcher.utils.file_paths import resource_path


class SubstringMatcherCli:
    """
    Creates instances of a command line interface that allows users to
    interact with the Substring Matcher based on a set of choices.
    """

    def __init__(self):
        self.trie: Trie = None
        self.trie_builder: TrieBuilder = TrieBuilder()
        self.user_input: str = ""
        self.keyword_input: str = ""
        self.url_input: str = ""
        self.keywords: list[str] = []
        self.urls: list[str] = []
        self.keyword_search_results: dict = {}
        self.invalid_keywords = []

    def start_cli(self):
        """Welcomes the user and presents a menu."""
        display_welcome_message()
        user_input = input("Press the 'Enter' or 'Return' key to continue.")

        display_menu_options_for_keyword_source()
        self.request_user_input()
        self.handle_response_to_keyword_options()

    def request_user_input(self):
        """Requests input from the user."""
        display_reminder_for_exiting_the_application()
        self.user_input = input("\nPlease enter your choice: ")

    def handle_response_to_keyword_options(self):
        """
        Handles what to do when a user provides a
        choice for the keyword options menu.
        """
        if self.user_input == '1':
            display_waiting_message_while_building_trie()
            self.trie_builder.file_name = DEFAULT_KEYWORDS_FILE
            self.trie, self.invalid_keywords = self.trie_builder.build_trie_from_file()
            self.trie_builder.invalid_keywords = []
            self.handle_displaying_invalid_keywords_message()
            display_ready_message_for_finding_keywords_in_url()
            display_menu_options_for_url_source()
            self.request_user_input()
            self.handle_response_to_url_options()

        elif self.user_input == '2':
            self.request_keywords()
            self.handle_keyword_input()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            display_menu_options_for_keyword_source()
            self.request_user_input()
            self.handle_response_to_keyword_options()

    def request_keywords(self):
        """
        Requests a list of keywords from the user
        through the command line.
        """
        self.clear_keyword_input_and_keywords()
        display_help_tips_for_keyword_input()
        self.keyword_input = input('Your keywords: ')

    def clear_keyword_input_and_keywords(self):
        """Clears the following instance variables."""
        self.keyword_input = ''
        self.keywords = []

    def handle_keyword_input(self):
        """
        Handles what happens when a user responds to the
        request for user defined keywords through the
        command line.
        """
        if self.keyword_input.strip():
            self.create_keyword_lists_from_user_input()
            self.request_keyword_confirmation()
            self.handle_keyword_confirmation()
        else:
            display_warning_to_request_more_keywords()
            self.request_keywords()
            self.handle_keyword_input()

    def create_keyword_lists_from_user_input(self):
        for keyword in self.keyword_input.lower().split('|'):
            formatted_keyword = keyword.strip()

            if formatted_keyword != '':
                self.add_keyword_to_appropriate_list(formatted_keyword)

    def add_keyword_to_appropriate_list(self, formatted_keyword):
        if self.is_valid_keyword(formatted_keyword):
            self.keywords.append(formatted_keyword)
        else:
            self.invalid_keywords.append(formatted_keyword)

    @staticmethod
    def is_valid_keyword(keyword):
        return bool(re.match("^[A-Za-z_-]*$", keyword))

    def request_keyword_confirmation(self) -> str:
        display_confirmation_message_for_keywords(
            self.keywords, self.invalid_keywords
        )
        self.user_input = input('Continue?: ')

    def handle_keyword_confirmation(self):
        """
        Handles behavior pertaining to user
        responses to the request for keyword confirmation.
        """
        if self.user_input.lower() in VALID_RESPONSES_FOR_YES:
            display_waiting_message_while_building_trie()
            self.trie_builder.user_keywords = self.keywords
            self.trie, self.invalid_keywords = self.trie_builder.build_trie_from_list()
            self.trie_builder.invalid_keywords = []
            self.handle_displaying_invalid_keywords_message()
            display_ready_message_for_finding_keywords_in_url()
            display_menu_options_for_url_source()
            self.request_user_input()
            self.handle_response_to_url_options()

        elif self.user_input.lower() in VALID_RESPONSES_FOR_NO:
            self.request_keywords()
            self.handle_keyword_input()
            self.handle_keyword_confirmation()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            self.handle_keyword_input()
            self.handle_keyword_confirmation()

    def handle_response_to_url_options(self):
        """
        Handles what to do when a user provides a
        choice for the URL options menu.
        """
        if self.user_input == '1':
            display_waiting_message_during_keyword_matching()
            self.search_urls_file_for_matching_keywords(DEFAULT_URLS_FILE)
            display_search_completion_notification()
            self.process_search_results_data_for_json_file()
            self.process_search_results_data_for_text_file()
            self.handle_displaying_search_results_summary()
            self.handle_restarting_cli_on_completion()

        elif self.user_input == '2':
            self.request_urls()
            self.handle_url_input()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            display_menu_options_for_url_source()
            self.request_user_input()
            self.handle_response_to_url_options()

    def request_urls(self):
        """Requests urls from the user through the command line."""
        self.reset_urls_and_url_input()
        display_help_tips_for_url_input()
        self.url_input = input('Your URLs: ')

    def handle_url_input(self):
        """
        Handles what happens when a user responds to the
        request for user defined URLs through the
        command line.
        """
        if self.url_input.strip():
            self.create_url_list()
            self.request_url_confirmation()
            self.handle_url_confirmation()
        else:
            display_warning_to_request_more_urls()
            self.request_urls()
            self.handle_url_input()

    def create_url_list(self):
        """Creates a list of URLs from the user's input"""
        self.urls = [url.strip()
                     for url in self.url_input.lower().split('|') if url.strip() != '']

    def request_url_confirmation(self) -> str:
        """
        Requests confirmation from the user regarding
        the list of urls provided.
        """
        display_confirmation_message_for_urls(self.urls)
        self.user_input = input('Enter yes or no (y/n): ')

    def handle_url_confirmation(self):
        """
        Handles behavior pertaining to user
        responses to the request for URL confirmation.
        """
        if self.user_input.lower() in VALID_RESPONSES_FOR_YES:
            display_waiting_message_during_keyword_matching()
            self.search_url_list_for_matching_keywords()
            display_search_completion_notification()
            self.process_search_results_data_for_json_file()
            self.process_search_results_data_for_text_file()
            self.handle_displaying_search_results_summary()
            self.handle_restarting_cli_on_completion()

        elif self.user_input.lower() in VALID_RESPONSES_FOR_NO:
            self.request_urls()
            self.handle_url_input()
            self.handle_url_confirmation()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            self.handle_url_input()
            self.handle_url_confirmation()

    def reset_urls_and_url_input(self):
        """Resets the values for the url and its input"""
        self.url_input = ''
        self.urls = []

    def search_urls_file_for_matching_keywords(self, file_name: str = DEFAULT_URLS_FILE) -> dict:
        """
        Iterates through a file containing URLs to find matching keywords.
        """
        if not isinstance(file_name, str):
            raise TypeError

        if not file_name.lower().endswith('.txt'):
            print("Make sure you are using a text file. The extension must be .txt")

        urls_file_path: str = resource_path(
            f"substring_matcher/data/{file_name}")

        with open(urls_file_path, 'r', encoding='utf-8') as urls_file:
            for url in urls_file:
                self.current_url = url
                self.add_keyword_match_data_to_search_results(url.strip())

    def search_url_list_for_matching_keywords(self) -> dict:
        """
        Iterates through a list of URLs to find matching keywords.
        """
        if not isinstance(self.urls, list):
            raise TypeError

        for url in self.urls:
            self.current_url = url
            self.add_keyword_match_data_to_search_results(url)

    def add_keyword_match_data_to_search_results(self, url: str):
        """
        Adds and matching keywords in the URL to the
        self.keyword_search_results dictionary for the
        specified URL.
        """
        self.keyword_search_results[url]: dict = {}
        self.keyword_search_results[url]['matches']: list = self.trie.find_matching_substrings(
            url)

        self.keyword_search_results[url][
            'runtime']: str = f"{self.calculate_keyword_search_runtime(url)} milliseconds"

    def calculate_keyword_search_runtime(self, url: str):
        start_time = datetime.datetime.now()
        self.trie.find_matching_substrings(url)
        end_time = datetime.datetime.now()
        runtime: int = (end_time - start_time).total_seconds() * 1000

        return runtime

    def process_search_results_data_for_json_file(self):
        search_results_json_path: str = resource_path(
            "substring_matcher/results/keyword_search_results.json")

        if os.path.exists(search_results_json_path):
            os.remove(search_results_json_path)

        with open(search_results_json_path, 'w') as json_file:
            self.write_url_keyword_match_data_to_file_as_json(json_file)

    def write_url_keyword_match_data_to_file_as_json(self, json_file):
        json_data = json.dumps(self.keyword_search_results, indent=3)
        json_file.write(json_data)

    def process_search_results_data_for_text_file(self):
        search_results_text_path: str = resource_path(
            "substring_matcher/results/keyword_search_results.txt")

        if os.path.exists(search_results_text_path):
            os.remove(search_results_text_path)

        with open(search_results_text_path, 'w') as text_file:
            self.write_url_keyword_match_data_to_file_as_text(text_file)

    def write_url_keyword_match_data_to_file_as_text(self, text_file):
        original_stdout = sys.stdout
        sys.stdout = text_file

        for url, data in self.keyword_search_results.items():
            display_url_keyword_match_data_in_file(
                url, data.get('matches'), data.get('runtime')
            )

        sys.stdout = original_stdout

    def handle_displaying_search_results_summary(self):
        """
        Loops over a list of URLs and displays the URL
        along with any matching keywords, if any.
        """
        urls_with_matching_keywords = [
            url for url, data in self.keyword_search_results.items() if data.get('matches')]

        total_number_of_urls: int = len(self.keyword_search_results)
        number_of_urls_with_matches: int = len(urls_with_matching_keywords)

        display_search_results_summary(
            total_number_of_urls,
            number_of_urls_with_matches
        )

    def handle_displaying_invalid_keywords_message(self):
        if self.invalid_keywords:
            display_invalid_keyword_info(
                len(self.invalid_keywords),
                self.invalid_keywords
            )
        else:
            print('All keywords are valid!')

    def handle_restarting_cli_on_completion(self):
        """
        Handles what happens once the program finishes
        running (i.e. searching URLs for matches).
        """
        self.reset_values()
        display_options_for_starting_over()
        self.request_user_input()
        self.handle_user_response_for_starting_over()

    def handle_user_response_for_starting_over(self):
        if self.user_input == '1':
            self.start_cli()

        elif self.user_input == '2':
            display_menu_options_for_url_source()
            self.request_user_input()
            self.handle_response_to_url_options()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            self.handle_restarting_cli_on_completion()

    def check_if_user_wants_to_exit(self):
        """
        Checks and exits if the user has provided 'exit' or 'quit'
        as the input through the command line.
        """
        if self.user_input in ['exit', 'quit']:
            display_farewell_message()
            sys.exit()

    def reset_values(self):
        """Resets all values to their default state."""
        self.user_input = ""
        self.keyword_input = ""
        self.url_input = ""
        self.keywords = []
        self.urls = []
        self.keyword_search_results = {}


def main():
    new_cli_instance = SubstringMatcherCli()
    new_cli_instance.start_cli()
