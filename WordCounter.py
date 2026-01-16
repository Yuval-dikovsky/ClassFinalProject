"""
Finds how many times a given word exists in a given text file. Case insensetive
option 4
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


if __name__ == "__main__":
    #flow
    counter = WordCounter(input("Enter a File Path: "))
    word_to_find = input("Enter a Word: ")
    #checks that the word is alphabetical
    if word_to_find.isalpha():
        result = counter.word_stats(word_to_find.lower())
        if result:
            print(f"The word exists {result} times.")
    else:
        print("The word you entered does not meet the criteria.")