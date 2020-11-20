import os

from trie import Trie


def build_trie_from_file() -> Trie:
    """
    Retrieves the keywords file, iterates through the keywords,
    then removes the newline from each keyword and adds it to the Trie.
    """

    trie: Trie = Trie()
    working_directory: str = os.getcwd()
    keywords_file_path: str = f"{working_directory}/substring_matcher/data/keywords.txt"

    with open(keywords_file_path, 'r', encoding='utf-8') as keywords_file:
        for keyword in keywords_file:
            trie.add_keyword(keyword.rstrip('\n'))

    return trie


def build_trie_from_list(keywords: list) -> Trie:
    """
    Iterates through the provided list of keywords
    and adds each one to the Trie.
    """

    trie: Trie = Trie()

    for keyword in keywords:
        trie.add_keyword(keyword.lower())

    return trie
