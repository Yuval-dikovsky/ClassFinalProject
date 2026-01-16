"""
Reads text from a given file and turns it into a list of words.
handles file errors
"""


import re
class TextProcessor:
    #initiating the object
    def __init__(self, file_path):
        self.file_path = file_path
        #Initializing the internal storage
        self.raw_text = ""
        self.word_list = []

    def get_file_path(self):
        # gets the file path
        return self.file_path

    def set_file_path(self, new_file_path):
        # sets new file path
        self.file_path = new_file_path

    def extract_text(self):
        """
        Extracts the text from the file path.
        Returns the text or false if something goes wrong.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.raw_text = file.read()
                return True
        except FileNotFoundError:
            return False, "File not found. Please enter a valid file path."
        except PermissionError:
            return False, "Permission denied. Please enter a valid file path."
        except Exception as e:
            return False, f"An unexpected error occurred: {e}"

    def normalized_text(self):
        """
        Takes a string and returns a list of words or None if the result is empty.
        *Space, tab, newline,comma, -, _ , :, ; are treated as delimiters.
        """
        self.word_list = re.split(r'[\s,\-_:;]+', self.raw_text.strip().lower())
        return self.word_list


