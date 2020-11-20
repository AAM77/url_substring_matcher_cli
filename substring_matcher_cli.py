#!/usr/bin/env python3

import os

from substring_matcher.trie import Trie, TrieNode
from substring_matcher.trie_builders import build_trie_from_file, build_trie_from_list


class SubstringMatcherCli:
    """
    It's something that does something else.
    """

    def __init__(self):
        self.trie: Trie = None
        self.user_input = ""
        self.keywords = []
        self.urls = []
        self.keyword_search_results: dict = {}

    def run_cli(self):
        self.welcome_user()
        user_input = input("Press the 'Enter' or 'Return' key to continue.")
        self.display_keyword_options()
        self.handle_response_to_keyword_options()

    def welcome_user(self):
        print('#####################################')
        print('#                                   #')
        print('# WELCOME TO THE SUBSTRING MATCHER! #')
        print('#                                   #')
        print('#####################################\n')
        print('This is an application that help you determine if a URL contains keywords you are interested in.\n')
        print('--------------------------------------\n')

    def check_if_user_wants_to_exit(self):
        if self.user_input in ['exit', 'quit']:
            print("Thank you for using the Substring Matcher!")
            print("Goodbye!")
            quit()

    def display_incorrect_response_alert(self):
        print('Please enter a valid choice.')
        print("Or, enter 'exit' or 'quit' to close the program.")

    def display_keyword_options(self):
        print('\nPlease choose how you want to supply the keywords:')
        print('[1] Use the keywords.txt file.')
        print('[2] Provide a list of keywords.')
        print('\n')
        print("Note: Enter '1' or '2'.")

    def handle_response_to_keyword_options(self):
        self.user_input = input("Please enter your choice: ")

        if self.user_input == '1':
            print('One moment while we load your keywords into the system...')
            self.trie = build_trie_from_file(
                'substring_matcher/data/keywords.txt')
            print('You are now ready to search URLs for keywords.')
            self.display_url_options()
            self.handle_response_to_url_options()

        elif self.user_input == '2':
            self.request_keywords()

            if self.user_input:
                self.handle_keyword_confirmation()
        else:
            self.check_if_user_wants_to_exit()
            self.display_incorrect_response_alert()
            self.handle_response_to_keyword_options()

    def request_keywords(self):
        self.user_input = ''
        self.keywords = []

        print("\nEnter keywords separated by a space")
        self.user_input = input('Your keywords: ')

    def handle_keyword_confirmation(self):
        self.keywords = self.user_input.split(' ')
        print(f'\nAre {self.keywords} the keywords you entered?')

        self.user_input = input('Enter yes or no (y/n): ')

        if self.user_input.lower() in ['y', 'yes']:
            print('\nOne moment while we load your keywords into the system...')
            self.trie = build_trie_from_list(self.keywords)
            print('You are now ready to search URLs for keywords.')
            self.display_url_options()
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
        self.user_input = input("Please enter your choice: ")

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
            self.handle_response_to_url_options()

    def request_urls(self):
        self.user_input = ''
        self.urls = []

        print("\nEnter URLs separated by a space")
        self.user_input = input('Your URLs: ')

    def handle_url_confirmation(self):
        self.urls = self.user_input.split(' ')
        print(f'\nAre {self.urls} the URLs you entered?')

        self.user_input = input('Enter yes or no (y/n): ')

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
        Iterates through the URLs for matches.
        """

        if not isinstance(file_path, str):
            raise TypeError

        working_directory: str = os.getcwd()
        urls_file_path: str = f"{working_directory}/{file_path}"

        with open(urls_file_path, 'r', encoding='utf-8') as urls_file:
            for url in urls_file:
                self.keyword_search_results[url]: list = self.trie.find_matching_substrings(
                    url)

    def search_url_list_for_matching_keywords(self) -> dict:
        """
        Iterates through the URLs for matches.
        """

        if not isinstance(self.urls, list):
            raise TypeError

        for url in self.urls:
            self.keyword_search_results[url]: list = self.trie.find_matching_substrings(
                url)

    def display_url_search_results(self):
        for url, matching_keywords in self.keyword_search_results.items():
            print("\n######################################")
            print("######################################\n")
            print(f"URL: {url}")
            print("\nMATCHING KEYWORDS:")
            print(matching_keywords)
            print("\n######################################")
            print("######################################\n")
            print("\n")

    def final_message(self):
        print("Thank you for using this substring matcher.")
        print("Please type 'exit' or 'quit' to end the program.")
        user_input = input("> ")


new_cli_instance = SubstringMatcherCli()
new_cli_instance.run_cli()
