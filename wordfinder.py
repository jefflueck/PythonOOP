"""Word Finder: finds random words from a dictionary."""
# Need to review with mentor.
import random

class WordFinder:

    def __init__(self, phrase):

        word_file = open(phrase)

        self.words = self.parse(word_file)

        print(f'{len(self.words)} words read')

    def parse(self, word_file):
        return[w.strip() for w in word_file]

    def random(self):
        return random.choice(self.words)




