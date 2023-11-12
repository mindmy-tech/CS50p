import sys
from tabulate import tabulate
import csv

def main():
    len_argv = len(sys.argv)
    if len_argv < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len_argv > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        argv = sys.argv[1]

        if not argv.endswith('.csv'):
            print("Not a CSV file")
            sys.exit(1)

        try:
            with open(argv) as f:
                menu = []
                reader = csv.reader(f)
                for row in reader:
                    menu.append(row)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)

        print(tabulate(menu[1:], menu[0], tablefmt="grid"))


main()