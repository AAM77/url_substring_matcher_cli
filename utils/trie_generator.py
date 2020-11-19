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

    def build_all(self, root):
        trie_word_list = []
        if root:
            if root.children:
                for node in root.children.values():
                    for char in self.build_all(node):
                        trie_word_list.append(str(node.letter) + char)
            else:
                trie_word_list.append('')
        return trie_word_list


new_trie = Trie()
keywords = ['apple', 'app', 'jello', 'gel', 'caps', 'capitols']

for keyword in keywords:
    new_trie.add_keyword(keyword)

print(new_trie.build_all(new_trie.root))
