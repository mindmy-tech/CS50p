camelCase = input("camelCase : ")
word =""
snake_case = ""
for letter in camelCase:
    if letter.isupper():
        snake_case += f"{word}_"
        word = letter.lower()
    else:
        word += letter
snake_case += word
print(f"snake_case: {snake_case}")