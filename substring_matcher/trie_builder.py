from substring_matcher.constants import SUBSTRING_MATCHER_DATA_PATH
from substring_matcher.utils.file_paths import resource_path
from substring_matcher.trie import Trie
import os
import re


class TrieBuilder:

    def __init__(self):
        self.file_name: str = ""
        self.user_keywords: list = []
        self.invalid_keywords: list = []
        self.trie: Trie = Trie()
        self.current_normalized_keyword: str = ""

    def build_trie_from_file(self) -> tuple:
        """
        Retrieves the keywords file, iterates through the keywords,
        then removes the newline from each keyword and adds it to the 
        Trie.

        For this method, the self.file_name should be the name of the
        keywords file stored inside of the data folder, which resides 
        inside of the substring_matcher app.
        """
        if not isinstance(self.file_name, str):
            raise TypeError

        if not self.file_name.lower().endswith('.txt'):
            raise ValueError("File extension must be .txt")

        keywords_file_path: str = resource_path(
            f"{SUBSTRING_MATCHER_DATA_PATH}/{self.file_name}")
        self.process_keywords_file(keywords_file_path)
        self.reset_current_normalized_keyword()

        return (self.trie, self.invalid_keywords)

    def process_keywords_file(self, keywords_file_path: str):
        """
        Opens the file and processes the keywords by adding 
        the keyword to the Trie if it is valid. It closes
        the file once finished.
        """
        with open(keywords_file_path, 'r', encoding='utf-8') as keywords_file:
            for keyword in keywords_file:
                self.current_normalized_keyword = keyword.lower().strip()
                self.filter_valid_keywords()

    def build_trie_from_list(self) -> tuple:
        """
        Iterates through the provided list of keywords
        and adds each one to the Trie.
        """
        if not isinstance(self.user_keywords, list):
            raise TypeError

        for keyword in self.user_keywords:
            self.current_normalized_keyword = keyword.lower().strip()
            self.filter_valid_keywords()

        self.reset_current_normalized_keyword()

        return (self.trie, self.invalid_keywords)

    def filter_valid_keywords(self):
        """
        Adds valid keywords to the trie and
        move invalid keywords to a separate list.
        """
        if not isinstance(self.current_normalized_keyword, str):
            raise TypeError

        if self.is_valid_keyword():
            self.trie.add_keyword(self.current_normalized_keyword)
        else:
            self.invalid_keywords.append(self.current_normalized_keyword)

    def is_valid_keyword(self) -> bool:
        """
        Returns True if the keyword is valid.
        A valid keywords contains only alpha
        characters, underscores, and/or hyphens.
        All other words are invalid.
        """
        if not isinstance(self.current_normalized_keyword, str):
            raise TypeError

        return bool(re.match("^[A-Za-z_-]*$", self.current_normalized_keyword))

    def reset_current_normalized_keyword(self):
        self.current_normalized_keyword = ""
