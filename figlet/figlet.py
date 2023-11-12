from pyfiglet import Figlet
import sys


args = sys.argv
if len(args) > 1:
    if args[1] in ['-f', '-font']:
        try:
            figlet = Figlet(font= args[2])
        except :
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    figlet = Figlet()

input_str = input("Input: ")
ascii_text = figlet.renderText(input_str)

print("Output: ")
print(ascii_text)