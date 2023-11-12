from os.path import splitext
from PIL import Image, ImageOps
import sys

def main():
    args = sys.argv[1:]
    len_args = len(args)

    if len_args < 2:
        sys.exit("Too few command-line arguments")
    elif len_args > 2:
        sys.exit("Too many command-line arguments")

    input_img = args[0]
    output_img = args[1]

    input_extention , output_extention = splitext(input_img)[1], splitext(output_img)[1]

    valid_extentions = [".jpeg",".jpg",".png"]

    # print(input_extention.lower())

    if not input_extention.lower() in valid_extentions:
        sys.exit("Invalid input")

    if not input_extention.lower() == output_extention.lower():
        sys.exit("Input and output have different extensions")


    shirt = Image.open("shirt.png", mode='r')

    try:
        input_image = Image.open(input_img, mode='r')
        size = shirt.size

        input_image = ImageOps.fit(input_image, size, bleed=0.0, centering=(0.5, 0.5))
        print("here")
        input_image.paste(shirt, shirt)

        input_image.save(output_img)

    except FileNotFoundError:
        sys.exit("Invalid input")

main()