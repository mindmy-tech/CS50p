import random

def main():
    level = get_level()
    print(generate_integer(level))

def get_level():
    while True:
        level = input()
        if level in ['1', '2', '3']:
            return(int(level))

def generate_integer(level):
    score = 0
    for _ in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        else:
            x = random.randint(pow(10, level - 1), pow(10, level) - 1)
            y = random.randint(pow(10, level - 1), pow(10, level) - 1)
        z = x + y
        print(x, '+', y, '=')
        counter = 0

        while True:
            if counter == 3:
                print(x, '+', y, '=', z)
                break
            try:
                answer = int(input())
                if answer != z:
                    print('EEE')
                    counter += 1
                else:
                    score += 1
                    break

            except ValueError:
                pass
    return(score)

if __name__ == '__main__':
    main()