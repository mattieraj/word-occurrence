import unittest
import word_occurrence


class TestHashmapInsertion(unittest.TestCase):

    def test_hashmap_newitem(self):
        hashmapTest={}
        #test inserttohashmap for hashmap insertion of new (unique) items
        word_occurrence.insertToHashmap(hashmapTest, "hello")
        word_occurrence.insertToHashmap(hashmapTest, "goodbye")
        self.assertEqual({"hello":1, "goodbye":1},
                    hashmapTest)


    def test_hashmap_duplicates(self):
    #test for updating frequencies (duplicates)
        hashmapTest={}
        word_occurrence.insertToHashmap(hashmapTest, "duplicate")
        word_occurrence.insertToHashmap(hashmapTest, "unique")
        word_occurrence.insertToHashmap(hashmapTest, "duplicate")
        word_occurrence.insertToHashmap(hashmapTest, "duplicate")
        self.assertEqual({"duplicate":3, "unique":1}, hashmapTest)