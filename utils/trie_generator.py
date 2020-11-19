import os
import datetime


class TrieNode:
    """This docstring is EMPTY!"""

    def __init__(self, letter: str):
        self.letter: str = letter
        self.children: dict = {}
        self.is_end_of_word: bool = False


class Trie:
    """This docstring is EMPTY!"""

    def __init__(self):
        self.root: TrieNode = TrieNode("*")

    def add_keyword(self, keyword: str):
        """This docstring is EMPTY!"""

        current_node: TrieNode = self.root

        for letter in keyword:
            if letter not in current_node.children:
                current_node.children[letter]: TrieNode = TrieNode(letter)
            current_node = current_node.children[letter]

        current_node.is_end_of_word = True

    def does_word_exist(self, word: str) -> bool:
        """This docstring is EMPTY!"""

        if word == "":
            return True

        current_node: TrieNode = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]

        return current_node.is_end_of_word

    def build_trie_word_list(self, node: TrieNode) -> list:
        trie_words: list = []
        if node:
            if node.children:
                for child_node in node.children.values():
                    for char in self.build_trie_word_list(child_node):
                        trie_words.append(str(child_node.letter) + char)
            else:
                trie_words.append('')
        return trie_words

    """
    PSEUDOCODE

    accept a url string as an argument
    create a variable to hold the current matching substring.
    create an array of matching substrings

    iterate through the url
    for each character in the url, look for a match in the trie that we built earlier
        if there is a match:
            - (1) concat the character to the matching_substr variable
            - (2) check to to see if Trie.is_end_of_word is True
                - (a1) if it is True:
                    - (i) append the value of the matching_substr variable to the matching_substrings array/list.
                    - (ii) reassign matching_substr to be an empty string

                - (b) check if the current node has children
                    - (T) if yes, then we reassign the current node to be one that matches the character (and allow the iteration to continue)
                    - (F) (else) if not, then reset the current node to be the root node

                - (a2) (else) if not, then we leave the current node as is and allow the iteration to continue

        else, if not (there is no match):
            - then reset the current node to be the root


    return the array of matching substrings (keywords)
    """

    def find_matching_substrings(self, url: str) -> list:
        if url == "":
            return []

        current_substring = ''
        matching_keywords = []
        current_node: TrieNode = self.root  # root

        for index, character in enumerate(url):  # p

            if current_node.is_end_of_word:  # True
                matching_keywords.append(current_substring)

            if character in current_node.children:  # {}
                current_substring = ''.join((current_substring, character))
                current_node = current_node.children[character]

            else:
                current_substring = ''
                current_node = self.root

        return matching_keywords


new_trie = Trie()
keywords = ['apple', 'app', 'jello', 'gel', 'caps', 'capitols']

working_directory = os.getcwd()
keywords_file_path = working_directory + '/data/keywords.txt'

with open(keywords_file_path, 'r', encoding='utf-8') as keywords_file:
    for keyword in keywords_file:
        print(keyword.rstrip('\n'))
        new_trie.add_keyword(keyword.rstrip('\n'))


runtimes = []

for _ in range(100000):
    start_time = datetime.datetime.now()
    print(new_trie.does_word_exist('zwitterionic'))
    end_time = datetime.datetime.now()

    runtime = (end_time - start_time).total_seconds() * 1000

    runtimes.append(runtime)

average_runtime = sum(runtimes)/(len(runtimes))

print(f"Runtime is: {average_runtime} ms")
