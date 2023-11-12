import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # pattern to check for 4 subnets
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    if match := re.search(pattern, ip.strip()):
        for i in range(1, 5):
            if not int(match.group(i)) <= 255:return False
        return True
    return False

if __name__ == "__main__":
    main()