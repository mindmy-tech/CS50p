from termcolor import colored
from nltk.corpus import words
from art import text2art
import time
import random
import sys
import shutil

class terminalArt: 
    def __init__(self,staticWord="", DynamicWord="Wordle" ):
        self.staticWord = staticWord
        self.DynamicWord = DynamicWord
        self.welcomeLoader()

    def count_newlines(self, text):
        newline_count = 0
        for char in text:
            if char == '\n':
                newline_count += 1
        return newline_count
    
    def center_text(self,text):
        terminal_width, _ = shutil.get_terminal_size()
        lines = text.split('\n')
        centered_lines = [line.center(terminal_width) for line in lines]

        return '\n'.join(centered_lines)
    
    def welcomeLoader(self):

        frames = [colored(self.center_text(text2art(f"{self.staticWord} {self.DynamicWord[0:i]}")), "red") for i in range(len(self.DynamicWord))]
        frames += [colored(self.center_text(text2art(f"{self.staticWord} {self.DynamicWord}")), "green")]
        for frame in frames:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.1)
            num_lines = self.count_newlines(frame)
            time.sleep(0.1)
            for _ in range(num_lines):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
        
        sys.stdout.write("\r" + frames[len(frames ) -1])


terminal_Art = terminalArt()
def main():

    while True:
        try:
            wordsize = int(input("Enter the WordSize: "))
            if wordsize<4 or wordsize>8:
                print(colored("The size should be between 4 -> 8", "red"))
            else:
                break
        except ValueError:
            print(colored("Enter a digit !", "red"))
    
    word = get_random_word(wordsize)
    print(f"the word {word} ")
    tries = wordsize + 1
    win = False


    for _ in range(tries):
        score = 0
        guess = get_word(wordsize)
        status = [0 for i in range(wordsize)]
        status = check_word(guess, wordsize, status, word)
        print_guess(guess, status, wordsize)

        for i in range(wordsize):
            score += status[i]
        if score == wordsize * 2:
            win = True
            break
    
    if win:
        print(colored(text2art("You Won"), "green"))
    else:
        print(colored(text2art(f"The Word was '{word}' "), "red"))



def is_valid_word(word):
    valid_word_set = set(words.words())
    return word.lower() in valid_word_set

def get_random_word(wordsize):
    word_list = words.words()
    word = [word for word in word_list if len(word) == wordsize]
    return random.choice(word)

def get_word(wordsize):
    while True:
        guess = input(f"Input a {wordsize}-letter word: ")
        if len(guess) == wordsize:
            if is_valid_word(guess):
                return guess
            print("Thats not a word")
        else:
            print(f"Enter a {wordsize}-letter word")

def check_word(guess, wordsize, status, word):
    for i in range(wordsize):
        for j in range(wordsize):
            if i == j and guess[i].lower() == word[i].lower():
                status[i] = 2
                break

            elif guess[i] == word[j]:
                status[i] = 1
    return status

def print_guess(guess, status, WordSize):
    for i in range(WordSize):
        if status[i] == 2:
            print(colored(guess[i], "green"), end="")
        elif status[i] == 1:
            print(colored(guess[i], "yellow"), end="")
        else:
            print(colored(guess[i], "red"), end="")
    print()

if __name__ == "__main__":
    main()
