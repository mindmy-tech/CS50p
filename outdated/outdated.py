months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def ISO_8601(year, month, day):
    try:
        month, day, year = int(month), int(day), int(year)
    except ValueError:
        ...
    else:
        if day <= 31 and month <= 12:
            print(f"{year}-{month:02}-{day:02}")
            return True
    return False

while True:
    try:
        date = input(": ").strip()
    except EOFError:
        print()
        break
    middle_endian = date.split("/")
    anno_domini = date.split(",")

    if len(middle_endian) == 3:
        month, day, year = middle_endian
        if ISO_8601(year, month, day):
            break
        continue

    elif len(anno_domini) == 2:
        month, day = anno_domini[0].split(" ")
        try:
                month = months.index(month.title()) + 1
        except ValueError:
            ...
        else:
            year = anno_domini[1]
            if ISO_8601(year, month, day):
                break
