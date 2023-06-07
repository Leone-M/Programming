import tkinter as tk
import tkinter.messagebox as msg
import random

class Main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guess numb")

        self.quest_numb = random.randint(1,100)
        self.tries = 0


        self.quest_label = tk.Label(text="Guess number in range of 1 and 100")
        self.quest_label.grid(row=0, column=0, columnspan=3)

        self.entry = tk.Entry(validate="all", validatecommand=(self.register(self.validate), "%P"))
        self.entry.grid(row=1, column=0, columnspan=3)
        self.usernumb = "0"

        self.guess_button = tk.Button(text="Try", command=self.guess)
        self.guess_button.grid(row=2, column=1)

        self.restart_button = tk.Button(text="Restart", command=self.restart)
        self.restart_button.grid(row=2, column=0)

        self.tries_button = tk.Button(text="Number of tries", command=self.show_tries)
        self.tries_button.grid(row=2, column=2)

        self.wrong_text = tk.StringVar()
        self.wrong_lable = tk.Label(textvariable=self.wrong_text)
        self.wrong_lable.grid(row=3, column=0, columnspan=3)    

    def validate(self, line: str):
        for e in line:
            if e not in "1234567890": return False
        if line != "" and (int(line) > 100 or int(line) == 0):
            return False
        return True
    
    def guess(self):
        self.usernumb = int(self.entry.get())
        if self.usernumb == self.quest_numb:
            self.wrong_text.set(f"Bingo! Answer was {self.quest_numb}")
        else:
            self.tries += 1
            if self.usernumb < self.quest_numb:
                self.wrong_text.set("Lower than need")
            elif self.usernumb > self.quest_numb:
                self.wrong_text.set("Greater than need")

    def restart(self):
        self.tries = 0
        self.quest_numb = random.randint(1, 100)
        self.wrong_text.set("Number changed, tries reseted")

    def show_tries(self):
        self.wrong_text.set(f"You tried to guess number {self.tries} times")
    
        

window = Main_window()
tk.mainloop()