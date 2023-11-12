
def main():
    fuel_fraction = input("Fraction : ")
    print(gauge(convert(fuel_fraction)))


def convert(fraction):
        try:
            x, y = fraction.split("/")

            x , y = int(x), int(y)
            fuel = round(x * 100 / y)

        except (ValueError, ZeroDivisionError):
            exit(1)
        return fuel



def gauge(fuel):
    if fuel <= 1:
        return "E"
    elif fuel >= 99:
        return "F"
    else:
        return f"{fuel}%"



if __name__ == "__main__":
    main()
