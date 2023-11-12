
groceryList = {}

while True:
    try:
        item = input("").upper()
    except EOFError:
        print()
        for items in sorted(groceryList.items()):
            print(f"{items[1]} {items[0]}")
        break
    if item in groceryList:
        groceryList[item] += 1
    else:
        groceryList[item] = 1
