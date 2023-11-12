def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Psedocode

    # plate should consist of 6 chars
    if len(plate) > 6  or len(plate) < 2:
        return False

    # plate[0] and plate[1] are alpha
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # for char in plate:
    for i in range(len(plate)):
        #   char.isalpha or char.digit()
        if plate[i].isalpha():
            continue
        elif plate[i].isdigit():
            # if digit found try converting the rest string to int if success return valid else not valid
            if plate[i] == '0':
                return False
            try:
                int(plate[i:6])
                return True
            except:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    main()


