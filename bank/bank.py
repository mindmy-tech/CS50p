reply = input("Greetings :").lower().strip()
balance = "$0"
if reply[0:5] == "hello":
    balance = "$0"
elif reply[0] == 'h':
    balance = "$20"
else:
    balance = '$100'
print(balance)