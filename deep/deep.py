val = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
ans_list = ['42','forty two', 'forty-two']

if val.lower().strip() in ans_list:
    print("Yes")
else:
    print("No")