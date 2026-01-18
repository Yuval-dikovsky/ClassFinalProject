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
        Raises an exception if the target word is not alphabetic.
        """
        if not target_word.isalpha():
            raise ValueError("word must contain only alphabetic characters")
        self.process_text_to_word_list()
        return self.word_list.count(target_word.lower())

