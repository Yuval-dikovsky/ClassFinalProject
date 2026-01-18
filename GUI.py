
#Imports for GUI
import tkinter
from tkinter import scrolledtext, simpledialog
from art import text2art

#Import threading for HTTP server
import threading

#Imports from my project modules
import TopWords, PC_Stats, NetworkCheck, WordCounter, HttpServer

"""
Provied a GUI menu of option to the user
1. Counts words occurrences in a file, sorts them and displays the top 5 in a table.
2. Provide the full information about the PC and public IP details
3. Checks network connection
4. Finds how many times a given word exists in a given text file.
5. Creates HTTP server on the local computer. The HTTP server contains the Pictures directory and its sub-directories.
6. Exits the script
"""

class MenuGUI:
    #Initiate the GUI class
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.geometry("1200x760")
        self.gui_setup()

    def gui_setup(self):
        """
        Defines all the widgets needed for the menu, and places them in the main window.
        """
        #welcome widget
        welcome_text = text2art("WELCOME", font="block", chr_ignore=True)
        self.label_welcome = tkinter.Label(self.root, text=welcome_text, font=("Courier", 8), fg="black")
        self.label_welcome.pack(pady=10)

        # Buttons Frame
        button_frame = tkinter.Frame(self.root)
        button_frame.pack(pady=10)
        buttons = [
            ("Option 1: Top Words", self.option1_top_words),
            ("Option 2: PC Stats", self.option2_pc_stats),
            ("Option 3: Network Check", self.option3_network_check),
            ("Option 4: Word Counter", self.option4_word_counter),
            ("Option 5: HTTP Server", self.option5_http_server),
            ("Option 6: Exit", self.root.destroy)
        ]
        #Unpacking the buttons and creating them
        for text, command in buttons:
            if text == "Option 6: Exit":
                tkinter.Button(button_frame,text=text,width=40,command=command,bg="#E74C3C",fg="white").pack(pady=5)
            else:
                tkinter.Button(button_frame,text=text,width=40,command=command).pack(pady=5)

        #Output area
        self.result_area = scrolledtext.ScrolledText(self.root, width=120, height=30)
        self.result_area.pack(pady=10)

    def print_output(self, string):
        """
        print strings to the window
        """
        #inserts the string at the end of the text box
        self.result_area.insert(tkinter.END, str(string) + "\n")

    def clear_output(self):
        """
        Clears the output area
        """
        self.result_area.delete('1.0', tkinter.END)

    def option1_top_words(self):
        """
        Counts words occurrences in a file, sorts them and displays the top 5 in a table.
        """
        self.clear_output()
        file_path = simpledialog.askstring("File path", "Enter full file path:")
        #Handles user clicking cancel
        if not file_path:
            return
        self.print_output(f"Processing top words for: {file_path}")
        try:
            top_words = TopWords.TopWords(file_path)
            display = top_words.display_top_words()
            self.print_output(display)
        except FileNotFoundError:
            self.print_output("File not found. Please enter a valid file path")
        except PermissionError:
            self.print_output("Permission denied. Please enter a valid file path")
        except UnicodeDecodeError:
            self.print_output("Unicode error. Please enter a valid file path")
        except Exception as e:
            self.print_output(f"Unexpected error: {e}")

    def option2_pc_stats(self):
        """
        Provide the full information about the PC and public IP details
        """
        self.clear_output()
        try:
            self.print_output("Gathering PC specs and IP details...")
            specs = PC_Stats.pc_specs()
            self.print_output(specs)
        except Exception:
            self.print_output("Error: can't get PC specs")
        try:
            self.print_output("---------------------")
            self.print_output("IP Details:")
            ip = PC_Stats.ip_details()
            self.print_output(ip)
        except Exception:
            self.print_output("Error: can't gather IP details")


    def option3_network_check(self):
        """
        Checks network connection
        """
        self.clear_output()
        try:
            self.print_output("Checking network connection...")
            network_status = NetworkCheck.network_check()
            self.print_output(f"Network status: {network_status}")
        except Exception as e:
            self.print_output(f"Unexpected error: {e}")

    def option4_word_counter(self):
        """
        Finds how many times a given word exists in a given text file.
        """
        self.clear_output()
        file_path = simpledialog.askstring("File path", "Enter full file path for Word Counter:")
        if not file_path:
            return
        try:
            word_counter = WordCounter.WordCounter(file_path)
            word = simpledialog.askstring("Input", "Enter a Word to count:")
            if not word:
                return
            self.print_output(f"Counting '{word}' in: {file_path}")
            result = word_counter.word_stats(word)
            self.print_output(f"The word '{word}' exists {result} times.")
        except Exception as e:
            self.print_output(f"Error: {e}")

    def option5_http_server(self):
        """
        Creates HTTP server on the local computer. The HTTP server contains the Pictures directory and its sub-directories.
        """
        self.clear_output()
        def run_server():
            """
            Runs the server
            """
            try:
                server = HttpServer.PictureHTTPServer()
                port = server.get_port()
                self.print_output(f"Starting pictures HTTP Server at... http://127.0.0.1:{port}")
                #Attemps to starts the server in the function
                server.start_server()
            except Exception as e:
                self.print_output(f"Server Error: {e}")
        try:
            # Creates a thread with a daemon
            # without a daemon the user wont be able to close the program if he clicked on option5
            HTTP_thread = threading.Thread(target=run_server, daemon=True)
            HTTP_thread.start()
        except Exception as e:
            self.print_output(f"Unexpected error: {e}")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MenuGUI(root)
    root.mainloop()