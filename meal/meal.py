def main():
    time = input("whats the time: ")
    time = convert(time)
    if time >= 7 and time <=8:
        print("breakfast time")
    elif time >= 12 and time <=13:
        print("lunch time")
    elif time >= 18 and time <=19:
        print("dinner time")


def convert(time):
    hrs, mins = time.split(":")
    mins_dec = round (int(mins) / 60, 2)
    return int(hrs) + mins_dec


if __name__ == "__main__":
    main()