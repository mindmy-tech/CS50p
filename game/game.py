import random
while True:
    try:
        level =int(input("Level :"))
        if level <= 0:
            raise "NoNegative"
    except:
        pass
    else:
        break
r_num = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess :"))
        if guess <= 0 or guess > level:
            raise "NoNegative"
    except:
        ...
    else:
        if guess > r_num:
            print("Too large!")
        elif guess < r_num:
            print("Too Small!")
        else:
            print("Just Right!")
            break
