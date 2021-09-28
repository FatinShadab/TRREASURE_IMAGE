import argparse
import pathlib
import logging
from . import (
    PIRATE,
    EXPLORER,
    GifMaker,
    CONVERTER,
)


def main():

    # Docs. link
    link = "https://github.com/FatinShadab/TRREASURE_IMAGE/blob/main/README.md#cli-commands"

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding arguments
    parser.add_argument("Class", help = "enter the class name [PIRATE] | [CONVERTER] | [EXPLORER] | [GifMaker]  (ex: python/python3 -m treasure_image PIRATE)")

    # for class PIRATE and EXPLORER
    parser.add_argument("-hm", "--host_image", type=pathlib.Path, help = "enter the host image path.")
    parser.add_argument("-tt", "--treasure_type", type=str, help = "enter the treasure type [str] | [img] | [file] | [exe]")
    parser.add_argument("-t", "--treasure", help = "enter treasure")

    # for class CONVERTER
    parser.add_argument("-img", "--target_image", type=pathlib.Path, help = "enter the target image")
    parser.add_argument("-ft", "--format_to", type=str, help = "convert format like png , jpg etc")
    parser.add_argument("-file", "--target_file", type=pathlib.Path, help = "enter the target file(Must be a .text or.txt)")
    parser.add_argument("-ct", "--convert_to", type=str, help = "converted output script name with format like (example.py)")


    # for class GifMaker
    parser.add_argument("-imgs", "--imgs_folder", type=pathlib.Path, help="enter the path of images folder.")
    parser.add_argument("-if", "--img_format", type=str, help="enter format to filter select")
    parser.add_argument("-title", "--gif_title", type=str, help="enter the output gif title")
    parser.add_argument("-d", "--duration", type=int, help="enter the duration for each image to display")
    parser.add_argument("-l", "--loop", type=int, help="enter the number of loop as desired")


    args = parser.parse_args()


    if args.Class == "PIRATE":
        if  args.host_image:
            if  args.treasure_type == "str":
                try:
                    PIRATE.hide_str_treasure(f"{args.host_image}", f"{args.treasure}")
                except:
                    logging.error(f"Something went wrong check the docs: {link}")
            if args.treasure_type == "img":
                try:
                    PIRATE.hide_img_treasure(str(args.host_image), str(args.treasure))
                except:
                    logging.error(f"Something went wrong check the docs: {link}")
            if args.treasure_type == 'file' or args.treasure_type == 'exe':
                try:
                    PIRATE.hide_file_treasure(str(args.host_image), str(args.treasure))
                except:
                    logging.error(f"Something went wrong check the docs: {link}")


    if args.Class == "EXPLORER":
        if args.host_image:
            if  args.treasure_type == "str":
                try:
                    print(EXPLORER.seek_str_treasure(f"{args.host_image}"))
                except:
                    logging.error(f"Something went wrong check the docs: {link}")
            if args.treasure_type == "img":
                try:
                    EXPLORER.seek_img_treasure(f"{args.host_image}")
                except:
                    logging.error(f"Something went wrong check the docs: {link}")
            if args.treasure_type == "exe":
                try:
                    EXPLORER.seek_exe_treasure(str(args.host_image))
                except:
                    logging.error(f"Something went wrong check the docs: {link}")
            if args.treasure_type == "file":
                try:
                    EXPLORER.seek_file_treasure(str(args.host_image))
                except:
                    logging.error(f"Something went wrong check the docs: {link}")


    if args.Class == "CONVERTER":
        if args.target_image and args.format_to:
            try:
                CONVERTER.convert_image(target_image=str(args.target_image), format_to=str(args.format_to))
            except:
                logging.error(f"Something went wrong check the docs: {link}")
        if args.target_file and args.convert_to:
            try:
                CONVERTER.convert_to_script(text_file=str(args.target_file), convert_to=str(args.convert_to))
            except:
                logging.error(f"Something went wrong check the docs: {link}")


    if args.Class == "GifMaker":
        try:
            GifMaker(imgs_folder= args.imgs_folder,
                    image_formate= args.img_format,
                    title= args.gif_title,
                    duration= args.duration,
                    loop= args.loop).make_gif()
        except:
            logging.error(f"Something went wrong check the docs: {link}")
        


if __name__ == "__main__":
    main()