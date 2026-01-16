"""
Counts words occurrences in a file, sorts them and displays the top 5 in a table.
option1
"""


import TextProcessor
class TopWords(TextProcessor.TextProcessor):
    #initializing the class
    def __init__(self, file_path):
        super().__init__(file_path)

    def count_words(self):
        """
        Takes a list of words and counts how many times each word appears.
        Returns a dictionary of words and their counts.
        Returns an empty dictionary if there are no words.
        """
        if self.extract_text():
            self.normalized_text()
            word_dict_count = {}
            # Loops over the word list and increment the count of the word to its dictionary key. If the key doesn't exist yet, it creates it
            for word in self.word_list:
                #checks that the word only contains alphabetical characters
                if word.isalpha():
                    if word.lower() in word_dict_count:
                        word_dict_count[word] += 1
                    else:
                        word_dict_count[word] = 1
            return word_dict_count
        return {}

    def sort_words(self):
        """
        sorting the word by count and return the sorted list of words
        """
        word_dict_count = self.count_words()
        sorted_list = sorted(word_dict_count.items(), key=lambda item: item[1], reverse=True)
        return sorted_list

    def display_top_words(self):
        """
        displaying the top words and their count, maximum of 5 top words
        """
        sorted_list = self.sort_words()
        max_results = min(5, len(sorted_list))
        display = f"The top {max_results} reoccurring words are:\n"
        for i in range(max_results):
            word = sorted_list[i][0]
            count = sorted_list[i][1]
            display += f"{i + 1}. \"{word}\" with {count} occurrences\n"
        return display
#flow
if __name__ == "__main__":
    try:
        user_file_stats = TopWords(input("Please enter the full file path: "))
        if user_file_stats.count_words() != {}:
            print(user_file_stats.display_top_words())
        else:
            print("No valid words to display")
    except Exception as e:
        print(f"Unexpected error:, {e}")



