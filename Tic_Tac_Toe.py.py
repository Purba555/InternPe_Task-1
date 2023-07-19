import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.geometry("240x300")
        self.grid()

        self.symbols = ['X', 'O']
        self.current_symbol = 0
        self.buttons = []
        self.create_buttons()
        
    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self, text="", font=("Calibri", 36), width=3, height=1,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons.append(button)
    

    def on_button_click(self, row, col):
        button = self.buttons[row * 3 + col]
        if button["text"] == "":
            button["text"] = self.symbols[self.current_symbol]
            self.current_symbol = 1 - self.current_symbol
            if self.check_winner():
                self.disable_buttons()
                winner = self.symbols[1 - self.current_symbol]
                messagebox.showinfo("Winner", f"Winner: {winner}")
            elif self.check_draw():
                self.disable_buttons()
                messagebox.showinfo("Draw", "It's a draw!")

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if all(self.buttons[i]["text"] == self.symbols[0] for i in line):
                return True
            if all(self.buttons[i]["text"] == self.symbols[1] for i in line):
                return True
        return False

    def check_draw(self):
        return all(button["text"] != "" for button in self.buttons)

    def disable_buttons(self):
        for button in self.buttons:
            button["state"] = tk.DISABLED

    def reset_game(self):
        for button in self.buttons:
            button["text"] = ""
            button["state"] = tk.NORMAL
        self.current_symbol = 0

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
