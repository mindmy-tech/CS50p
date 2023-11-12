import validators

email = input("Enter your Email: ")
if validators.email(email):
    print("Valid")

else:
    print("Invalid")