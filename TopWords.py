"""
Counts words occurrences in a file, sorts them and displays the top 5 in a table.
"""
import sys

import TextProcessor
class TopWords(TextProcessor.TextProcessor):
    #initializing the class
    def __init__(self, file_path):
        self.word_dict_count = {}
        super().__init__(file_path)

    def count_words(self):
        """
         Takes a list of words and counts how many times each word appears
         Returns a dictionary of words and their counts
         Returns None if there are no words
         """
        self.process_text_to_word_list()
        # Loops over the word list and increment the count of the word to its dictionary key. If the key doesn't exist yet, it creates it
        for word in self.word_list:
            #checks that the word only contains alphabetical characters
            if word.isalpha():
                if word.lower() in self.word_dict_count:
                    self.word_dict_count[word] += 1
                else:
                    self.word_dict_count[word] = 1
        sorted_list = sorted(self.word_dict_count.items(), key=lambda item: item[1], reverse=True)
        return sorted_list

    def display_top_words(self):
        """
        Display top words (maximum 5 words) or the error message if something went wrong.
        """
        sorted_list = self.count_words()
        if len(sorted_list) == 0:
            return "No top words found"
        max_results = min(5, len(sorted_list))
        display = f"The top {max_results} reoccurring words are:\n"
        for i in range(max_results):
            word = sorted_list[i][0]
            count = sorted_list[i][1]
            display += f"{i + 1}. \"{word}\" with {count} occurrences\n"
        return display

if __name__ == '__main__':
    try:
        obj = TopWords("C:\\Users\\User\\Downloads\\Final Exercise Python 2026.htmlggg").display_top_words()
        print(obj)
    except Exception as e:
        print(f"Unexpected error: {e}. \nPlease enter a valid file path")