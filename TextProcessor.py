"""
Reads text from a given file and turns it into a list of words.
handles file errors
"""
import re
class TextProcessor:
    # initiating the object
    def __init__(self, file_path):
        self.file_path = file_path
        self.word_list = []
        #Reads the file in the init, throws exception if file unreadable
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
        Processes the text and turns it into a list of words
        Delimiter are white space,comma, -, _, :, ;
        return the list of words
        """
        self.word_list = re.split(r'[\s,\-_:;]+', self.raw_text.strip().lower())
        return self.word_list
