"""
Finds how many times a given word exists in a given text file. Case insensetive
"""

import TextProcessor
class WordCounter(TextProcessor.TextProcessor):
    #initalize the class
    def __init__(self, file_path):
        super().__init__(file_path)

    def word_stats(self, target_word):
        """
        Counts the number of times a given word exists in a given text file.
        Uses the TextProcessor class to first extract the word, normalize the text and count the number of times it exists.
        returns the number of times it exists.
        """
        if self.extract_text():
            self.normalized_text()
            return self.word_list.count(target_word)
        return None