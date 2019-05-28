import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="provide full path to file") #mandatory
     #optional flags
    parser.add_argument("-u", "--uniquewords", help="if number of unique words should be outputted: '-U'",
                        action="store_true")
    parser.add_argument("-w", "--wordSearched", type=str, help = "provide word: number of occurrences of "
                                                                 "word provided will be calculated")
    arg = parser.parse_args()
    filename =  arg.filename
    hashmap = file_parser(filename)


    # optional flags

    # on argument command, provides num of unique chars
    if arg.uniquewords:
        result = numUniqueWords(hashmap)
        print result

    #on argument command, provides freq of occurrence of word provided
    if arg.wordSearched:
        result = num_occurrences_word(hashmap, arg.wordSearched)
        print result,


def file_parser(filename):
    # This function parses through a file given as input and inserts each word into a hashmap.
    fp = None
    hashmap = {}

    try:
        fp = open(filename)
        for line in fp:
            words = parse_line(line)
            #iterate through list (words)
            for word in words:
                if word != "":
                    insertToHashmap(hashmap, word)  #ignore empty strings
    except Exception, ex:
        print("File does not exist"),
    finally:
        if fp is not None: fp.close()

    return hashmap


def parse_line(line):
    #helper method for file_parser
    return re.split(r'\s+|\.|!|,|\?', line.strip())

def insertToHashmap(hashmap, word):
    if hashmap.has_key(word):  # occurrence of word updated
        freq = hashmap.get(word)
        freq = freq + 1
        hashmap[word] = freq
    else:
        hashmap[word] = 1  # new word added


def numUniqueWords(hashmap):
    return len(hashmap)

def num_occurrences_word(hashmap, word):
    return hashmap.get(word)

if __name__ == '__main__':
    main()