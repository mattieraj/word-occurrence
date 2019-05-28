import unittest
import word_occurrence

class TestFlags(unittest.TestCase):

    def test_unique_char(self):
        hashmap = word_occurrence.file_parser("words.txt")
        self.assertEqual(15, word_occurrence.numUniqueWords(hashmap))

    def test_num_occurrences_word(self):
        hashmap = word_occurrence.file_parser("words.txt")
        self.assertEqual(2, word_occurrence.num_occurrences_word(hashmap, "bye"))

    def test_num_occurrences_two(self):
        hashmap = word_occurrence.file_parser("beloved.txt")
        self.assertEqual(2, word_occurrence.num_occurrences_word(hashmap, "smiled"))

    def test_num_occurrences_two(self):
        hashmap = word_occurrence.file_parser("beloved.txt")
        self.assertEqual(13, word_occurrence.num_occurrences_word(hashmap, "they"))
