import unittest
from trie import Trie, TrieNode
from trie_builders import build_trie_from_list


class TestTrieNode(unittest.TestCase):

    def test_create_success(self):
        trie_node = TrieNode('l')
        self.assertEqual(trie_node.letter, 'l')
        self.assertEqual(trie_node.children, {})
        self.assertEqual(trie_node.is_end_of_word, False)

    def test_create_fail(self):
        self.assertRaises(TypeError, TrieNode)
        self.assertRaises(TypeError, TrieNode, 2)


class TestTrie(unittest.TestCase):
    def test_create_success(self):
        trie = Trie()
        self.assertEqual(trie.root.letter, '*')
        self.assertTrue(isinstance(trie.root, TrieNode))

    def test_create_fail(self):
        self.assertRaises(TypeError, Trie, 2)
        self.assertRaises(TypeError, Trie, 'a')

    def test_add_keyword(self):
        trie = Trie()
        trie.add_keyword('hello')
        self.assertEqual(trie.build_trie_word_list(trie.root), ['hello'])
        self.assertRaises(TypeError, trie.add_keyword, 2)

    def test_does_word_exist(self):
        trie = Trie()
        trie.add_keyword('hello')
        self.assertTrue(trie.does_word_exist(''))
        self.assertTrue(trie.does_word_exist('hello'))
        self.assertFalse(trie.does_word_exist('he'))
        self.assertFalse(trie.does_word_exist('zebra'))
        self.assertRaises(TypeError, trie.does_word_exist, 2)

    def test_find_matching_substrings(self):
        keywords = ['arm', 'army', 'man', 'manly', 'manage',
                    'manager', 'management', 'woman', 'womanly']

        trie = build_trie_from_list(keywords)
        mixcase_url = 'http://www.Argonauts-Management.arM/find-managers/Woman/'
        lowercase_url = 'http://www.argonauts-management.arm/find-managers/woman/'

        self.assertTrue(isinstance(
            trie.find_matching_substrings(mixcase_url), list))

        self.assertTrue(isinstance(
            trie.find_matching_substrings(lowercase_url), list))

        self.assertEqual(trie.find_matching_substrings(mixcase_url), [
                         'arm', 'man', 'manage', 'management', 'manager', 'woman'])

        self.assertEqual(trie.find_matching_substrings(lowercase_url), [
                         'arm', 'man', 'manage', 'management', 'manager', 'woman'])


if __name__ == '__main__':
    unittest.main()
