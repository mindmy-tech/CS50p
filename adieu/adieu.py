from inflect import engine

p = engine()

names = []
sentence = "Adieu, adieu, to "
while True:
    try:
        input_name = input("name: ")
        names.append(input_name)
    except EOFError:
        print()
        break

name = p.join(names)
print(sentence + name)
