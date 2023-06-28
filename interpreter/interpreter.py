x, z, y = input("expression : ").split(" ")
x = float(x)
y = float(y)
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

match z:
    case "+":
        print(add(x, y))
    case "-":
        print(sub(x, y))
    case "*":
        print(mul(x, y))
    case "/":
        print(div(x, y))
    case _:
        print("invalid expression")