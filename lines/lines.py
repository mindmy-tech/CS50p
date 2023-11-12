import sys

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

        if not argv.endswith('.py'):
            print("Not a python file")
            sys.exit(1)

        try:
            with open(argv) as f:
                lines = []
                for line in f:
                    lines.append(line.strip())

        except FileNotFoundError:
            print("File not found")
            sys.exit(1)

        cnt = 0
        for line in lines:
            if line != "" and not line.startswith("#"):
                cnt += 1
        print(cnt)
main()