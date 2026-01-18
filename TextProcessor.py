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
        self.raw_text = ""
        self.word_list = []
        #stores error messages
        self.last_error = ""

    def get_file_path(self):
        # gets the file path
        return self.file_path

    def set_file_path(self, new_file_path):
        # sets new file path
        self.file_path = new_file_path

    def extract_text(self):
        """
        Extracts the text from the file path.
        Returns true if sucessful, false if something goes wrong.
        Sets self.last_error with the error message.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.raw_text = file.read()
                return True
        except FileNotFoundError:
            self.last_error = "File not found. Please enter a valid file path."
            return False
        except PermissionError:
            self.last_error = "Permission denied. Please enter a valid file path."
            return False
        except UnicodeDecodeError:
            self.last_error = "Unicode error. Please enter a valid file path."
        except Exception as e:
            self.last_error = f"Unexpected error: {e}"
            return False

    def normalized_text(self):
        """
        Takes a string and returns a list of words or None if the result is empty.
        *Space, tab, newline,comma, -, _ , :, ; are treated as delimiters.
        """
        if self.raw_text:
            self.word_list = re.split(r'[\s,\-_:;]+', self.raw_text.strip().lower())
        return self.word_list