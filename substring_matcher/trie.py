class TrieNode:
    """Each instance represents a node for the trie"""

    def __init__(self, letter: str):
        if not isinstance(letter, str):
            raise TypeError

        self.letter: str = letter
        self.children: dict = {}
        self.is_end_of_word: bool = False


class Trie:
    """Each instances represents the Trie tree that gets created"""

    def __init__(self):
        self.root: TrieNode = TrieNode("*")

    def add_keyword(self, keyword: str):
        """
        Adds the substring/keyword to the Trie by
        creating a separate node for each unique character
        """

        if not isinstance(keyword, str):
            raise TypeError

        current_node: TrieNode = self.root

        for letter in keyword.lower():
            if letter not in current_node.children:
                current_node.children[letter]: TrieNode = TrieNode(letter)
            current_node = current_node.children[letter]

        current_node.is_end_of_word = True

    def does_word_exist(self, word: str) -> bool:
        """
        Checks is the desired word exists inside the trie.
        This is used promarily for a list of strings, not a url.
        """

        if not isinstance(word, str):
            raise TypeError

        if word == "":
            return True

        current_node: TrieNode = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]

        return current_node.is_end_of_word

    def find_matching_substrings(self, url: str) -> list:
        """
        Creates a list/array to determine all of the matching substrings
        from the URL that is passed to it.
        """

        if not isinstance(url, str):
            raise TypeError

        if url == "":
            return []

        url = url.lower()
        current_substring: str = ''
        matching_keywords: list[str] = []
        current_node: TrieNode = self.root

        for index, outer_character in enumerate(url):
            if outer_character in current_node.children:
                current_substring += outer_character
                current_node = current_node.children[outer_character]

                # Iterates over the remaining part of the string
                # instead of starting at the beginning.
                for inner_character in url[index+1:]:
                    if current_node.is_end_of_word:
                        matching_keywords.append(current_substring)

                    if inner_character in current_node.children:
                        current_substring += inner_character
                        current_node = current_node.children[inner_character]

                    # resets variable values and breaks out of the inner loop
                    else:
                        current_substring = ''
                        current_node = self.root
                        break
                else:
                    if current_substring and current_node.is_end_of_word:
                        matching_keywords.append(current_substring)

        return sorted(list(set(matching_keywords)))

    def build_trie_word_list(self, node: TrieNode) -> list:
        """
        Builds a word list from the current Trie to determine all
        of the words that are inside it.
        """

        trie_words: list = []
        if node:
            if node.children:
                for child_node in node.children.values():
                    for char in self.build_trie_word_list(child_node):
                        trie_words.append(str(child_node.letter) + char)
            else:
                trie_words.append('')
        return trie_words
