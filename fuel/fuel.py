
while True:
    fuel_fraction = input("Fraction : ")

    try:
        x, y = fuel_fraction.split("/")

        x , y = int(x), int(y)
        if x > y:
            raise "Not Possible"
        fuel = round(x * 100 / y)

        if fuel <= 1:
            print("E")
        elif fuel >= 99:
            print("F")
        else:
            print(f"{fuel}%")
        break
    except:
        ...


