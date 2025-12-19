import tkinter as tk
import random
import os

WORD_FILE = os.path.join(os.path.dirname(__file__), "wordbank.txt")
MAX_ATTEMPTS = 7

BG = "#121212"
FG = "#e0e0e0"
ACCENT = "#ff5555"

def load_words():
    with open(WORD_FILE, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

class HangmanUI:
    def __init__(self, root):
        self.root = root
        self.root.title("The Hangman Game")
        self.root.geometry("600x650")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.words = load_words()
        self.score = 0
        self.streak = 0

        self.reset_game()

        self.title = tk.Label(root, text="THE HANGMAN GAME", font=("Arial", 20, "bold"), bg=BG, fg=FG)
        self.title.pack(pady=10)

        self.score_label = tk.Label(root, text="", font=("Arial", 12), bg=BG, fg=FG)
        self.score_label.pack()

        self.canvas = tk.Canvas(root, width=200, height=250, bg=BG, highlightthickness=0)
        self.canvas.pack(pady=10)

        self.word_label = tk.Label(root, text="", font=("Courier", 20), bg=BG, fg=FG)
        self.word_label.pack(pady=5)

        self.guessed_label = tk.Label(root, text="", font=("Arial", 12), bg=BG, fg=FG)
        self.guessed_label.pack(pady=5)

        self.info_label = tk.Label(root, text="", font=("Arial", 11), bg=BG, fg=FG)
        self.info_label.pack()

        self.update_display()
        self.draw_hangman()

        self.root.bind("<Key>", self.key_input)

    def reset_game(self):
        self.word = random.choice(self.words)
        self.guessed = set()
        self.attempts = 0
        self.game_over = False

    def update_display(self):
        display = " ".join(c.upper() if c in self.guessed else "_" for c in self.word)
        guessed = " ".join(sorted(self.guessed)).upper()

        self.word_label.config(text=f"Word: {display}")
        self.guessed_label.config(text=f"Guessed: {guessed}")
        self.info_label.config(text=f"Attempts Left: {MAX_ATTEMPTS - self.attempts} (Type letters)")
        self.score_label.config(text=f"Score: {self.score}   Streak: {self.streak}")

    def key_input(self, event):
        if self.game_over:
            return

        ch = event.char.lower()
        if not ch.isalpha() or len(ch) != 1:
            return

        if ch in self.guessed:
            return

        self.guessed.add(ch)

        if ch not in self.word:
            self.attempts += 1
            self.draw_hangman()

        self.update_display()
        self.check_game_end()

    def draw_hangman(self):
        self.canvas.delete("all")

        self.canvas.create_line(20, 230, 180, 230, fill=FG)
        self.canvas.create_line(50, 230, 50, 20, fill=FG)
        self.canvas.create_line(50, 20, 130, 20, fill=FG)
        self.canvas.create_line(130, 20, 130, 40, fill=FG)

        if self.attempts >= 1:
            self.canvas.create_oval(110, 40, 150, 80, outline=FG)

        if self.attempts >= 2:
            self.canvas.create_line(130, 80, 130, 150, fill=FG)

        if self.attempts >= 3:
            self.canvas.create_line(130, 100, 110, 130, fill=FG)

        if self.attempts >= 4:
            self.canvas.create_line(130, 100, 150, 130, fill=FG)

        if self.attempts >= 5:
            self.canvas.create_line(130, 150, 110, 190, fill=FG)

        if self.attempts >= 6:
            self.canvas.create_line(130, 150, 150, 190, fill=FG)

        if self.attempts >= 7:
            self.canvas.create_line(118, 50, 125, 57, fill=ACCENT)
            self.canvas.create_line(125, 50, 118, 57, fill=ACCENT)
            self.canvas.create_line(135, 50, 142, 57, fill=ACCENT)
            self.canvas.create_line(142, 50, 135, 57, fill=ACCENT)

    def check_game_end(self):
        if all(c in self.guessed for c in self.word):
            self.score += 1
            self.streak += 1
            self.end_game("YOU WIN!")
        elif self.attempts >= MAX_ATTEMPTS:
            self.streak = 0
            self.end_game(f"YOU LOSE!\nWord: {self.word.upper()}")

    def end_game(self, message):
        self.game_over = True
        popup = tk.Toplevel(self.root)
        popup.configure(bg=BG)
        popup.title("Game Over")
        popup.geometry("300x160")

        tk.Label(popup, text=message, font=("Arial", 14), bg=BG, fg=FG).pack(pady=20)
        tk.Button(
            popup,
            text="Next Game",
            bg=ACCENT,
            fg="black",
            command=lambda: [popup.destroy(), self.restart()]
        ).pack()

    def restart(self):
        self.reset_game()
        self.draw_hangman()
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    HangmanUI(root)
    root.mainloop()
