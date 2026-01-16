import NetworkCheck, HttpServer, PC_Stats, TopWords, WordCounter
import tkinter as tk

class options:

    def __init__(self):
        pass

    def clear_content(self):
        """Removes all widgets from the content frame to provide a clean slate."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def start_server(self):
        pass

    def networkCheck(self):
        # 1. Clear Screen
        self.clear_content()
        tk.Label(self.content_frame, text="Pinging google.com...", font=("Arial", 12)).pack(pady=20)
        self.root.update()

        # 2. Process
        result = NetworkCheck.network_check()

        # 3. Update Screen
        self.clear_content()
        color = "green" if "Connected" in result else "red"

        tk.Label(self.content_frame, text="Internet Connection Status:", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.content_frame, text=result, font=("Arial", 24, "bold"), fg=color).pack(pady=10)



    def topWords(self):
        pass

    def wordCounter(self):
        pass

    def PC_Stats(self):
        pass



