import unittest
import word_occurrence


class TestParseLine(unittest.TestCase):

    def test_with_punc(self):
        # test parse_line with punctuation
        self.assertEqual(['elephant','moose','giraffe','bird','Parakeet'],
                         word_occurrence.parse_line("elephant,moose!giraffe.bird?Parakeet"))


    def test_with_spaces(self):
        # test parse_line with multiple spaces
        self.assertEqual(['elephant','', 'moose', 'giraffe', 'bird','Parakeet'],
                         word_occurrence.parse_line("elephant, moose!giraffe.bird    Parakeet"))


    def test_with_no_delimiters(self):
        # test parse_line with no delimiters
        self.assertEqual(['thisisonewordelephantmoosegiraffebirdParakeet'],
                         word_occurrence.parse_line(
                             "thisisonewordelephantmoosegiraffebirdParakeet"))