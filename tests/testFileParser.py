import word_occurrence
import unittest


class TestFileParser(unittest.TestCase):

    def test_file_parser_DNE(self):
        # test for file that does not exist
        hashmapResult = word_occurrence.file_parser("fakefile.txt")
        self.assertEqual({}, hashmapResult)

    def test_file_parser(self):
        #test with words.txt
        hashmapResult = word_occurrence.file_parser("words.txt")
        self.assertEqual({"hello":1, "world":1, "good":1, "bye":2, "Willy": 1, "Wonka": 1, "Charlie": 1,
                          "and": 1, "the":1, "Chocolate":1, "Factory":1, "moose":1, "goat":1, "Helen":1,
                          "Hunt":1}, hashmapResult)


