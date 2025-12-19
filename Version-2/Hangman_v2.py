import random
import os

TITLE = '''
                                                █░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 
                                                █▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 
                                                ░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀                                                    

████████╗██╗  ██╗███████╗    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
╚══██╔══╝██║  ██║██╔════╝    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
   ██║   ███████║█████╗      ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗  
   ██║   ██╔══██║██╔══╝      ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
   ██║   ██║  ██║███████╗    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
'''

WIN_ART = '''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
'''

LOSE_ART = '''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
'''

STAGES = [
    '''
   +---+
       |
       |
       |
       |
     ===''',
    '''
   +---+
   |   |
   O   |
       |
       |
     ===''',
    '''
   +---+
   |   |
   O   |
   |   |
       |
     ===''',
    '''
   +---+
   |   |
   O   |
  /|   |
       |
     ===''',
    '''
   +---+
   |   |
   O   |
  /|\  |
       |
     ===''',
    '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
     ===''',
    '''
   +---+
   |   |
   X   |
  /|\  |
  / \  |
     ==='''
]

MAX_ATTEMPTS = len(STAGES) - 1
WORD_FILE = "wordbank.txt"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    print(TITLE)

def load_words():
    with open(WORD_FILE, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

def get_word(words):
    return random.choice(words)

def display(word, guessed, attempts):
    clear()
    print(STAGES[attempts])
    print("\nWord:", " ".join(c if c in guessed else "_" for c in word))
    print("Guessed:", " ".join(sorted(guessed)))
    print("Attempts left:", MAX_ATTEMPTS - attempts)

def play(words):
    word = get_word(words)
    guessed = set()
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        display(word, guessed, attempts)

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            continue

        if guess in guessed:
            continue

        guessed.add(guess)

        if guess not in word:
            attempts += 1

        if all(c in guessed for c in word):
            clear()
            print(WIN_ART)
            print("WORD:", word)
            return

    clear()
    print(STAGES[-1])
    print(LOSE_ART)
    print("WORD WAS:", word)


def main():
    try:
        words = load_words()
    except FileNotFoundError:
        print("wordbank.txt not found!")
        return

    while True:
        clear()
        choice = input("PLAY ? (yes or no): ").lower().strip()
        if choice not in ("yes", "y"):
            break
        play(words)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
