fullSentence = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O' ,'U']
shortSentence = ""
for letter in fullSentence:
    if letter not in vowels:
        shortSentence += letter

print(f"Output: {shortSentence}")