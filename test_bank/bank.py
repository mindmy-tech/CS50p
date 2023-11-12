def main():
    reply = input("Greetings :").lower().strip()
    balance = value(reply)
    print(f'${balance}')

def value(reply):
    if reply[0:5] == "hello":
        balance = 100
    elif reply[0] == 'h':
        balance = 20
    else:
        balance = 0
    return balance


if __name__ == "__main__":
    main()