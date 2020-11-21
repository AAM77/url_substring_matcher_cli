#!/usr/bin/env python3

import json
import sys
import os

from constants import (
    DEFAULT_KEYWORDS_FILE,
    DEFAULT_URLS_FILE,
    VALID_RESPONSES_FOR_NO,
    VALID_RESPONSES_FOR_YES
)
from trie import Trie, TrieNode
from trie_builders import build_trie_from_file, build_trie_from_list
from utils.cli_messages import (
    display_farewell_message,
    display_incorrect_response_alert,
    display_menu_options_for_keyword_source,
    display_menu_options_for_url_source,
    display_welcome_message
)


class SubstringMatcherCli:
    """
    Creates instances of a command line interface that allows users to
    interact with the Substring Matcher based on a set of choices.
    """

    def __init__(self):
        self.trie: Trie = None
        self.user_input: str = ""
        self.keyword_input: str = ""
        self.url_input: str = ""
        self.keywords: list[str] = []
        self.urls: list[str] = []
        self.keyword_search_results: dict = {}
        self.working_directory: str = os.getcwd()

    def start_cli(self):
        """Welcomes the user and presents a menu."""
        display_welcome_message()
        user_input = input("Press the 'Enter' or 'Return' key to continue.")

        display_menu_options_for_keyword_source()
        self.request_user_input()
        self.handle_response_to_keyword_options()

    def reset_values(self):
        """Resets all values to their default state."""
        self.user_input = ""
        self.keyword_input = ""
        self.url_input = ""
        self.keywords = []
        self.urls = []
        self.keyword_search_results = {}

    def does_user_want_to_start_over(self):
        """
        Handles what happens once the program finishes
        running (i.e. searching URLs for matches).
        """
        print("Do you want to:")
        print("[1] Start from the beginning")
        print("[2] Provide different URLs")
        self.request_user_input()

        if self.user_input == '1':
            self.reset_values()
            self.start_cli()

        elif self.user_input == '2':
            display_menu_options_for_url_source()
            self.request_user_input()
            self.handle_response_to_url_options()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            self.does_user_want_to_start_over()

    def request_user_input(self):
        """Requests input from the user."""

        print(">>> Reminder: Enter 'exit' or 'quit' to exit the program. <<<")
        self.user_input = input("\nPlease enter your choice: ")

    def check_if_user_wants_to_exit(self):
        """
        Checks and exits if the user has provided 'exit' or 'quit'
        as the input through the command line.
        """
        if self.user_input in ['exit', 'quit']:
            display_farewell_message()
            quit()

    def handle_response_to_keyword_options(self):
        """
        Handles what to do when a user provides a
        choice for the keyword options menu.
        """
        if self.user_input == '1':
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('\nOne moment while we load your keywords into the system...')
            self.trie = build_trie_from_file(DEFAULT_KEYWORDS_FILE)
            print('You are now ready to search URLs for keywords.')
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

    def clear_keyword_input_and_keywords(self):
        """Clears the following instance variables."""
        self.keyword_input = ''
        self.keywords = []

    def request_keywords(self):
        """
        Requests a list of keywords from the user
        through the command line.
        """
        self.clear_keyword_input_and_keywords()

        print("\nEnter keywords separated by pipes (i.e. ' | ' ).")
        print("Example 1: Hello|Hi|welcome")
        print("Example 2: Hello | Hi | welcome")
        print("NOTE: Whitespace (e.g. spaces) will get stripped out since they do not belong in a url.\n")
        self.keyword_input = input('Your keywords: ')

    def create_keyword_list(self):
        self.keywords = [keyword.strip(
        ) for keyword in self.keyword_input.lower().split('|') if keyword != '']

    def request_keyword_confirmation(self) -> str:
        print(f'\nAre {self.keywords} the keywords you entered? (y/n)')
        self.user_input = input('Enter yes or no (y/n): ')

    def handle_keyword_input(self):
        """
        Handles what happens when a user responds to the
        request for user defined keywords through the
        command line.
        """
        if self.keyword_input.strip():
            self.create_keyword_list()
            self.request_keyword_confirmation()
            self.handle_keyword_confirmation()
        else:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!! You must provide at least one keyword. !!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            self.request_keywords()
            self.handle_keyword_input()

    def handle_keyword_confirmation(self):
        """
        Handles behavior pertaining to user
        responses to the request for keyword confirmation.
        """
        if self.user_input.lower() in VALID_RESPONSES_FOR_YES:
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('\nOne moment while we load your keywords into the system...')
            self.trie = build_trie_from_list(self.keywords)
            print('You are now ready to search URLs for keywords.')
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
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("\nOne moment while we search the URLs for keyword matches...")
            self.search_urls_file_for_matching_keywords(DEFAULT_URLS_FILE)
            print("\nDONE! Here are your results:")
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            self.send_matching_keywords_data_to_json_file()
            self.send_matching_keywords_data_to_text_file()
            self.display_url_search_results_summary()
            self.does_user_want_to_start_over()

        elif self.user_input == '2':
            self.request_urls()
            self.handle_url_input()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            display_menu_options_for_url_source()
            self.request_user_input()
            self.handle_response_to_url_options()

    def reset_urls_and_url_input(self):
        """Resets the values for the url and its input"""
        self.url_input = ''
        self.urls = []

    def request_urls(self):
        """Requests urls from the user through the command line."""
        self.reset_urls_and_url_input()

        print("\nEnter URLs separated by pipes (i.e. ' | ' ).")
        print("Example 1: http://Hello.com|Hi.net|www.welcome.com")
        print("Example 2: http://Hello.com | Hi.net | www.welcome.com")
        print("NOTE: Whitespace (e.g. spaces) will get stripped out since they do not belong in a url.\n")
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
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!! You must provide at least one URL. !!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            self.request_urls()
            self.handle_url_input()

    def create_url_list(self):
        """Creates a list of URLs from the user's input"""
        self.urls = [url.strip()
                     for url in self.url_input.lower().split('|') if url != '']

    def request_url_confirmation(self) -> str:
        """
        Requests confirmation from the user regarding
        the list of urls provided.
        """
        print(f'\nAre {self.urls} the urls you entered? (y/n)')
        self.user_input = input('Enter yes or no (y/n): ')

    def handle_url_confirmation(self):
        """
        Handles behavior pertaining to user
        responses to the request for URL confirmation.
        """
        if self.user_input.lower() in VALID_RESPONSES_FOR_YES:
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("\nOne moment while we search the URLs for keyword matches...")
            self.search_url_list_for_matching_keywords()
            print("\nDONE! Here are your results:")
            self.display_url_search_results()
            self.does_user_want_to_start_over()

        elif self.user_input.lower() in VALID_RESPONSES_FOR_NO:
            self.request_urls()
            self.handle_url_input()
            self.handle_url_confirmation()

        else:
            self.check_if_user_wants_to_exit()
            display_incorrect_response_alert()
            self.handle_url_input()
            self.handle_url_confirmation()

    def search_urls_file_for_matching_keywords(self, file_name: str = DEFAULT_URLS_FILE) -> dict:
        """
        Iterates through a file containing URLs to find matching keywords.
        """
        if not isinstance(file_name, str):
            raise TypeError

        if not file_name.lower().endswith('.txt'):
            print("Make sure you are using a text file. The extension must be .txt")

        urls_file_path: str = f"{self.working_directory}/data/{file_name}"

        with open(urls_file_path, 'r', encoding='utf-8') as urls_file:
            for url in urls_file:
                self.add_keyword_matches_to_search_results(url.strip())

    def search_url_list_for_matching_keywords(self) -> dict:
        """
        Iterates through a list of URLs to find matching keywords.
        """
        if not isinstance(self.urls, list):
            raise TypeError

        for url in self.urls:
            self.add_keyword_matches_to_search_results(url)

    def add_keyword_matches_to_search_results(self, url: str):
        """
        Adds and matching keywords in the URL to the
        self.keyword_search_results dictionary for the
        specified URL.
        """
        self.keyword_search_results[url]: list = self.trie.find_matching_substrings(
            url)

    def send_matching_keywords_data_to_json_file(self):
        matching_keywords_json_path = f"{self.working_directory}/results/matching_keywords.json"

        if os.path.exists(matching_keywords_json_path):
            os.remove(matching_keywords_json_path)

        with open(matching_keywords_json_path, 'w') as json_file:
            json_data = json.dumps(self.keyword_search_results, indent=3)
            json_file.write(json_data)

    def send_matching_keywords_data_to_text_file(self):
        original_stdout = sys.stdout

        matching_keywords_text_path = f"{self.working_directory}/results/matching_keywords.txt"

        if os.path.exists(matching_keywords_text_path):
            os.remove(matching_keywords_text_path)

        with open(matching_keywords_text_path, 'w') as matching_keywords_file:
            sys.stdout = matching_keywords_file

            for url, matching_keywords in self.keyword_search_results.items():
                print("\n######################################")
                print("######################################\n")
                print(f"URL: {url}")
                print("\nMATCHING KEYWORDS:")
                print(matching_keywords)
                print("\n######################################")
                print("######################################\n")
                print("\n")

            sys.stdout = original_stdout

    def display_url_search_results_summary(self):
        """
        Loops over a list of URLs and displays the URL
        along with any matching keywords, if any.
        """
        urls_with_matching_keywords = [
            url for url, matches in self.keyword_search_results.items() if matches]
        number_of_urls_with_matches = len(urls_with_matching_keywords)

        print("\n######################################")
        print("######################################")
        print(f"## Total number of urls: {len(self.keyword_search_results)}")
        print(f"## URLs with Matching Keywords: {number_of_urls_with_matches}")
        print("##")
        print("## See the 'results' directory in 'substring_matcher' for result details.")
        print("######################################")
        print("######################################\n")


new_cli_instance = SubstringMatcherCli()
new_cli_instance.start_cli()
