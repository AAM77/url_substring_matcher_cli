import sys
import unittest
from substring_matcher.trie import Trie, TrieNode
from substring_matcher.trie_builder import TrieBuilder
from substring_matcher.substring_matcher_cli import SubstringMatcherCli


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
    trie_builder = TrieBuilder()
    mixcase_url = 'http://www.Argonauts-Management.arM/find-managers/Woman/'
    lowercase_url = 'http://www.argonauts-management.arm/find-managers/woman/'
    url_ending_with_keyword_plus = 'http://www.argonauts-management.arm/find-managers/mississippi/womanlyon/'
    url_ending_with_only_keyword = 'http://www.argonauts-management.arm/find-managers/mississippi/womanlyon'
    invalid_url = """http://www.argonauts-management.arm/find-managers/mississippi/womanlyon/cathellohowhowdymeowsuper-catpurr-fectionsuper_meowword0word1word2word3word4word5word6word7word8word9meow!c@t#hello$how%howdy^meow&super-cat*purr-fection(super_meow)+meow=wow[hellohowdy]|absolute|ly\maybe/what/<sumsit>sanguine?~approximate`supercode`.wordscommas,"double'singlesymbol:analogycontinue-ish;{uniqueset}meow meow" "" "' '''"""

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

    def test_find_matching_substrings_from_list(self):
        keywords = ['arm', 'army', 'man', 'manly', 'manage',
                    'manager', 'management', 'woman', 'womanly']

        self.trie_builder.user_keywords = keywords

        trie, invalid_keywords = self.trie_builder.build_trie_from_list()

        self.assertTrue(isinstance(
            trie.find_matching_substrings(self.mixcase_url), list))

        self.assertTrue(isinstance(
            trie.find_matching_substrings(self.lowercase_url), list))

        self.assertEqual(trie.find_matching_substrings(self.mixcase_url), [
                         'arm', 'man', 'manage', 'management', 'manager', 'woman'])

        self.assertEqual(trie.find_matching_substrings(self.lowercase_url), [
                         'arm', 'man', 'manage', 'management', 'manager', 'woman'])

        self.assertEqual(
            trie.find_matching_substrings(self.url_ending_with_keyword_plus),
            ['arm', 'man', 'manage', 'management', 'manager', 'manly', 'mississippi',
             'woman', 'womanly', 'womanlyon']
        )

        self.assertEqual(
            trie.find_matching_substrings(self.url_ending_with_only_keyword),
            ['arm', 'man', 'manage', 'management', 'manager', 'manly', 'mississippi',
             'woman', 'womanly', 'womanlyon']
        )

        self.assertEqual(
            trie.find_matching_substrings(self.invalid_url),
            ['arm', 'cat', 'hello', 'how', 'howdy', 'man', 'manage', 'management',
             'manager', 'manly', 'meow', 'mississippi', 'purr-fection', 'super-cat',
             'super_meow', 'woman', 'womanly', 'womanlyon']
        )

    def test_find_matching_substrings_from_file(self):
        self.trie_builder.file_name = 'test_keywords.txt'
        trie, invalid_keywords = self.trie_builder.build_trie_from_file()

        self.assertTrue(isinstance(
            trie.find_matching_substrings(self.mixcase_url), list))

        self.assertTrue(isinstance(
            trie.find_matching_substrings(self.lowercase_url), list))

        self.assertEqual(trie.find_matching_substrings(self.mixcase_url), [
                         'arm', 'man', 'manage', 'management', 'manager', 'woman'])

        self.assertEqual(trie.find_matching_substrings(self.lowercase_url), [
                         'arm', 'man', 'manage', 'management', 'manager', 'woman'])

        self.assertEqual(
            trie.find_matching_substrings(self.url_ending_with_keyword_plus),
            ['arm', 'man', 'manage', 'management', 'manager', 'manly', 'mississippi',
             'woman', 'womanly', 'womanlyon']
        )

        self.assertEqual(
            trie.find_matching_substrings(self.url_ending_with_only_keyword),
            ['arm', 'man', 'manage', 'management', 'manager', 'manly', 'mississippi',
             'woman', 'womanly', 'womanlyon']
        )

        self.assertEqual(
            trie.find_matching_substrings(self.invalid_url),
            ['arm', 'cat', 'hello', 'how', 'howdy', 'man', 'manage', 'management',
             'manager', 'manly', 'meow', 'mississippi', 'purr-fection', 'super-cat',
             'super_meow', 'woman', 'womanly', 'womanlyon'])


class TestTrieBuilder(unittest.TestCase):

    trie_builder = TrieBuilder()

    def test_build_trie_from_file(self):
        self.trie_builder.file_name = 2
        self.assertRaises(
            TypeError,
            self.trie_builder.build_trie_from_file,
            self.trie_builder.file_name
        )

        self.trie_builder.file_name = 'some_file.txt'
        self.assertRaises(
            FileNotFoundError,
            self.trie_builder.build_trie_from_file)

        self.trie_builder.file_name = 'some_file'
        self.assertRaises(
            ValueError,
            self.trie_builder.build_trie_from_file
        )

        self.trie_builder.file_name = 'test_keywords.txt'
        self.assertTrue(
            isinstance(self.trie_builder.build_trie_from_file(), tuple)
        )

        expected_invalid_keywords = [
            '" "', '""', '"double', '#hello', '$how', '%howdy', '&super-cat', "' '", "''",
            "'single", '(super_meow)', '*purr-fection', '+meow', '.words', '/what/',
            '<sum', '=wow', '[hello', '\\maybe', '^meow', '`supercode`', 'c@t', 'commas,', 'continue-ish;',
            'howdy]', 'meow meow', 'meow!', 'sanguine?', 'set}', 'sit>', 'symbol:analogy', 'word0',
            'word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', '{unique',
            '|absolute|ly', '~approximate'
        ]

        self.trie_builder.invalid_keywords = []

        trie, invalid_keywords = self.trie_builder.build_trie_from_file()
        self.assertTrue(isinstance(trie, Trie))
        self.assertTrue(isinstance(invalid_keywords, list))
        self.assertTrue(len(invalid_keywords) > 0)
        self.assertEqual(sorted(invalid_keywords), expected_invalid_keywords)

    def test_build_trie_from_list(self):
        self.trie_builder.user_keywords = 'a'
        self.assertRaises(
            TypeError,
            self.trie_builder.build_trie_from_list,
            self.trie_builder.user_keywords
        )

        self.trie_builder.user_keywords = 2
        self.assertRaises(
            TypeError,
            self.trie_builder.build_trie_from_list,
            self.trie_builder.user_keywords
        )

        self.trie_builder.user_keywords = {}
        self.assertRaises(
            TypeError,
            self.trie_builder.build_trie_from_list,
            self.trie_builder.user_keywords
        )

        self.trie_builder.user_keywords = ['hi', 'hello', 'howdy']
        self.assertTrue(
            isinstance(self.trie_builder.build_trie_from_list(), tuple)
        )

        self.trie_builder.user_keywords = [
            'cat', 'hello', 'how', 'howdy', 'meow', 'super-cat', 'purr-fection',
            'super_meow', 'word0', 'word1', 'word2', 'word3', 'word4', 'word5',
            'word6', 'word7', 'word8', 'word9', 'meow!', 'c@t', '#hello', '$how',
            '%howdy', '^meow', '&super-cat', '*purr-fection', '(super_meow)',
            '+meow', '=wow', '[hello', 'howdy]', '|absolute|ly', '\\maybe',
            '/what/', '<sum', 'sit>', 'sanguine?', '~approximate', '`supercode`',
            '.words', 'commas,', '"double', "'single", "symbol:analogy", 'continue-ish;',
            '{unique', 'set}', 'meow meow', '" "', '""', "' '", "''"
        ]

        expected_invalid_keywords = [
            '" "', '""', '"double', '#hello', '$how', '%howdy', '&super-cat', "' '", "''",
            "'single", '(super_meow)', '*purr-fection', '+meow', '.words', '/what/',
            '<sum', '=wow', '[hello', '\\maybe', '^meow', '`supercode`', 'c@t', 'commas,', 'continue-ish;',
            'howdy]', 'meow meow', 'meow!', 'sanguine?', 'set}', 'sit>', 'symbol:analogy', 'word0',
            'word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', '{unique',
            '|absolute|ly', '~approximate'
        ]

        self.trie_builder.invalid_keywords = []
        self.trie_builder.trie = Trie()
        trie, invalid_keywords = self.trie_builder.build_trie_from_list()

        self.assertTrue(isinstance(trie, Trie))
        self.assertTrue(isinstance(invalid_keywords, list))
        self.assertTrue(len(invalid_keywords) > 0)
        self.assertEqual(sorted(invalid_keywords), expected_invalid_keywords)
