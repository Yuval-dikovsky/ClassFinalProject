"""
Reads text from a given file and turns it into a list of words.
handles file errors
"""
import re
class TextProcessor:
    # initiating the object
    def __init__(self, file_path):
        self.file_path = file_path
        # Initializing the internal storage
        self.word_list = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.raw_text = file.read()

    def get_file_path(self):
        # gets the file path
        return self.file_path

    def set_file_path(self, new_file_path):
        # sets new file path
        self.file_path = new_file_path

    def process_text_to_word_list(self):
        """
        Extracts the text from the file path.
        """
        self.word_list = re.split(r'[\s,\-_:;]+', self.raw_text.strip().lower())
        return self.word_list
    # def process_text_to_words(self):
    #     """
    #     Takes a string and returns a list of words or None if the result is empty.
    #     *Space, tab, newline,comma, -, _ , :, ; are treated as delimiters.
    #     """
    #     if self.raw_text:
    #         self.word_list = re.split(r'[\s,\-_:;]+', self.raw_text.strip().lower())
    #     return self.word_list