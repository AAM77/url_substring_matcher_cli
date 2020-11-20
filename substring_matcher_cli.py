#!/usr/bin/env python3

import os

from substring_matcher.trie import Trie, TrieNode
from substring_matcher.trie_builders import build_trie_from_file, build_trie_from_list


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

    def start_cli(self):
        """
        Welcomes the user and presents a menu.
        """
        self.display_welcome_message()
        user_input = input("Press the 'Enter' or 'Return' key to continue.")

        self.display_keyword_options()
        self.request_user_input()
        self.handle_response_to_keyword_options()
        self.does_user_want_to_start_over()

    def reset_values(self):
        """Resets all values to their default state"""
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
            self.display_url_options()
            self.request_user_input()
            self.handle_response_to_url_options()

        else:
            self.check_if_user_wants_to_exit()
            self.display_incorrect_response_alert()
            self.does_user_want_to_start_over()

    def display_welcome_message(self):
        """Displays a welcome message and warning. """
        print('#####################################')
        print('#                                   #')
        print('# WELCOME TO THE SUBSTRING MATCHER! #')
        print('#                                   #')
        print('#####################################\n')
        print('This is an application that helps you determine if a URL contains keywords you are interested in.\n')
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!                                                                               !!')
        print('!! ATTENTION: Please read the README.md for instructions on how to use this CLI. !!')
        print('!!                                                                               !!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        print('--------------------------------------\n')

    def request_user_input(self):
        """Requests input from the user."""
        self.user_input = input("Please enter your choice: ")

    def check_if_user_wants_to_exit(self):
        """
        Checks and exits if the user has provided 'exit' or 'quit'
        as the input through the command line.
        """
        if self.user_input in ['exit', 'quit']:
            self.display_final_message()
            quit()

    def display_final_message(self):
        print("\n**********************************************")
        print("* Thank you for using the Substring Matcher! *")
        print("* Goodbye!                                   *")
        print("**********************************************\n")

    def display_incorrect_response_alert(self):
        """
        Displays a message when the user selects and
        invalid choice.
        """
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!! Please enter a valid choice.                     !!')
        print("!! Or, enter 'exit' or 'quit' to close the program. !!")
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

    def display_keyword_options(self):
        """
        Displays a small menu with options related to how
        the user wants to provide the list of keywords.
        """
        print('\nPlease choose how you want to supply the keywords:')
        print('[1] Use the keywords.txt file.')
        print('[2] Provide a list of keywords.')
        print('\n')
        print("Note: Enter '1' or '2'.")

    def handle_response_to_keyword_options(self):
        """
        Handles what to do when a user provides a
        choice for the keyword options menu.
        """
        if self.user_input == '1':
            print('One moment while we load your keywords into the system...')
            self.trie = build_trie_from_file('keywords.txt')
            print('You are now ready to search URLs for keywords.')
            self.display_url_options()
            self.request_user_input()
            self.handle_response_to_url_options()

        elif self.user_input == '2':
            self.request_keywords()

            if self.user_input:
                self.handle_keyword_confirmation()
        else:
            self.check_if_user_wants_to_exit()
            self.display_incorrect_response_alert()
            self.display_keyword_options()
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

        print("\nEnter keywords separated by a space")
        self.keyword_input = input('Your keywords: ')

    def create_keyword_list(self):
        self.keywords = self.keyword_input.lower().split(' ')

    def request_keyword_confirmation(self) -> str:
        print(f'\nAre {self.keywords} the keywords you entered? (y/n)')
        self.user_input = input('Enter yes or no (y/n): ')

    def handle_keyword_confirmation(self):
        self.create_keyword_list()
        self.request_keyword_confirmation()

        if self.user_input.lower() in ['y', 'yes']:
            print('\nOne moment while we load your keywords into the system...')
            self.trie = build_trie_from_list(self.keywords)
            print('You are now ready to search URLs for keywords.')
            self.display_url_options()
            self.request_user_input()
            self.handle_response_to_url_options()

        elif self.user_input.lower() in ['n', 'no']:
            self.request_keywords()

            while not self.user_input:
                self.request_keywords()

            self.handle_keyword_confirmation()

        else:
            self.check_if_user_wants_to_exit()
            self.display_incorrect_response_alert()
            self.handle_keyword_confirmation()

    def display_url_options(self):
        print('\nPlease choose how you want to supply the URLs:')
        print('[1] Use the urls.txt file.')
        print('[2] Provide a list of urls.')
        print('\n')
        print("Note: Enter '1' or '2'.")

    def handle_response_to_url_options(self):
        if self.user_input == '1':
            print("\nOne moment while we search the URLs for keyword matches...")
            self.search_urls_file_for_matching_keywords(
                'substring_matcher/data/urls.txt')
            print("\nDONE! Here are your results:")
            self.display_url_search_results()

        elif self.user_input == '2':
            self.request_urls()

            if self.user_input:
                self.handle_url_confirmation()
        else:
            self.check_if_user_wants_to_exit()
            self.display_incorrect_response_alert()
            self.display_url_options()
            self.request_user_input()
            self.handle_response_to_url_options()

    def clear_url_input_and_urls(self):
        self.url_input = ''
        self.urls = []

    def request_urls(self):
        """Requests urls from the user through the command line."""
        self.clear_url_input_and_urls()

        print("\nEnter URLs separated by a space")
        self.url_input = input('Your URLs: ')

    def create_url_list(self):
        """Creates a list of URLs from the user's input"""
        self.urls = self.url_input.lower().split(' ')

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
        self.create_url_list()
        self.request_url_confirmation()

        if self.user_input.lower() in ['y', 'yes']:
            print("\nOne moment while we search the URLs for keyword matches...")
            self.search_url_list_for_matching_keywords()
            print("\nDONE! Here are your results:")
            self.display_url_search_results()

        elif self.user_input.lower() in ['n', 'no']:
            self.request_urls()

        else:
            self.check_if_user_wants_to_exit()
            self.display_incorrect_response_alert()
            self.handle_url_confirmation()

    def search_urls_file_for_matching_keywords(self, file_path: str) -> dict:
        """
        Iterates through a file containing URLs to find matching keywords.
        """

        if not isinstance(file_path, str):
            raise TypeError

        working_directory: str = os.getcwd()
        urls_file_path: str = f"{working_directory}/{file_path}"

        with open(urls_file_path, 'r', encoding='utf-8') as urls_file:
            for url in urls_file:
                self.add_keyword_matches_to_search_results(url)

    def search_url_list_for_matching_keywords(self) -> dict:
        """
        Iterates through a list of URLs to find matching keywords.
        """

        if not isinstance(self.urls, list):
            raise TypeError

        for url in self.urls:
            self.add_keyword_matches_to_search_results(url)

    def add_keyword_matches_to_search_results(self, url):
        """
        Adds and matching keywords in the URL to the
        self.keyword_search_results dictionary for the
        specified URL.
        """
        self.keyword_search_results[url]: list = self.trie.find_matching_substrings(
            url)

    def display_url_search_results(self):
        """
        Loops over a list of URLs and displays the URL
        along with any matching keywords, if any.
        """
        for url, matching_keywords in self.keyword_search_results.items():
            print("\n######################################")
            print("######################################\n")
            print(f"URL: {url}")
            print("\nMATCHING KEYWORDS:")
            print(matching_keywords)
            print("\n######################################")
            print("######################################\n")
            print("\n")


new_cli_instance = SubstringMatcherCli()
new_cli_instance.start_cli()
