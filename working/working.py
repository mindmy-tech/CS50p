import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = "(\d+(?::?\d+?)?)\s(\w+)\s(?:[toTO]+)\s(\d+(?::?\d+)?)\s(\w+)"
    if match := re.search(pattern, s):
        arr = [[match.group(1), match.group(2)], [match.group(3), match.group(4)]]
        valid_time = ['AM', 'PM']
        for i in range(2):
            if arr[i][1] in valid_time :
                time_ = '00'
                if ':' in arr[i][0]:
                    arr[i][0],time_ =arr[i][0].split(':')

                    if int(time_) >=60:
                        raise ValueError

                if arr[i][1] == 'AM':
                    if int(arr[i][0]) < 10:
                        arr[i][0] = f"0{arr[i][0]}"
                    elif int(arr[i][0]) == 12:
                        arr[i][0] = f"00"
                    arr[i][0] = f"{arr[i][0]}:{time_}"
                else:
                    if int(arr[i][0]) == 12:
                        arr[i][0] = f"00"
                    arr[i][0] = f"{int(arr[i][0]) + 12}:{time_}"
        return f"{arr[0][0]} to {arr[1][0]}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
