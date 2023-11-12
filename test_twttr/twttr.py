
def main():
    fullSentence = input("Input: ")
    shortSentence = shorten(fullSentence)
    print(f"Output: {shortSentence}")

def shorten(fullSentence):
    vowels = ['a', 'e', 'i', 'o', 'u' , '', 'E', 'I', 'O' ,'U']
    shortSentence = ""
    for letter in fullSentence:
        if letter not in vowels:
            shortSentence += letter
    return shortSentence


if __name__ == "__main__":
    main()