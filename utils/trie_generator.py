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

    def does_word_exist(self, word):
        """This docstring is EMPTY!"""

        if word == "":
            return True

        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]

        return current_node.is_end_of_word

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


runtimes = []

for i in range(100000):
    start_time = datetime.datetime.now()
    print(new_trie.does_word_exist('apps'))
    end_time = datetime.datetime.now()

    runtime = (end_time - start_time).total_seconds() * 1000

    runtimes.append(runtime)

average_runtime = sum(runtimes)/(len(runtimes))

print(f"Runtime is: {average_runtime} ms")
