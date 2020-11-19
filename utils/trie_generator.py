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
