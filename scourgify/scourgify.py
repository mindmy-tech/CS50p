import sys
import csv

def main():
    len_argv = len(sys.argv)
    if len_argv < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len_argv > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        argv = sys.argv[1]
        argv2 = sys.argv[2]

        if not argv.endswith('.csv') and argv2.endswith('.csv'):
            print("Not a CSV file")
            sys.exit(1)

        try:
            with open(argv) as f:
                data = []
                reader = csv.DictReader(f)
                for row in reader:
                    name = row['name']
                    house = row['house']
                    last, first = name.split(",")
                    person = {"first": first.strip(), "last": last.strip(), "house": house}
                    data.append(person)
        except FileNotFoundError:
            print(f"Could not read {argv}")
            sys.exit(1)

        # print(data)
        fields = ["first", "last", "house"]

        with open(argv2, 'w', newline='') as file:
             csv_writer = csv.DictWriter(file, fieldnames=fields)
             csv_writer.writeheader()
             csv_writer.writerows(data)

main()
