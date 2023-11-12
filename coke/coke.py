balance = 50
coins = [5, 10, 25]

while True:
    print(f"Amount Due: {balance}")
    coin = int(input("Insert coin: ").strip())
    if coin in coins:
        balance -= coin

    if balance <= 0:
        print(f"Change Owed: {-balance}")
        break