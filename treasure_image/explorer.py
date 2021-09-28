import logging
import PIL
from io import BytesIO
from PIL import Image


class EXPLORER:
    """
    ABOUT:
    --------
        The EXPLORER class is used to find hidden data from a host Image(type=jpg).

        Data that can be retrieve,

            # strings measseges
            # images (vector graphics are currently not supported!)
            # .exe files are handled separately
            # all type of files

    CONSTANT:
    ----------
            _SUPPORTED_TYPES: type --> tuple
            _UNSUPPORTED_TYPES: type --> tuple
            _READ_MODES: type --> tuple

    METHODS:
    ----------
        The methods of this class are:

            # seek_str_treasure --> extract hidden strings from host image(jpg)
            # seek_img_treasure --> extract hidden images from host image(jpg)
            # seek_exe_treasure --> extract hidden exe files from host image(jpg)
            # seek_file_treasure --> extract all hidden files from host image(jpg)
            in .txt format 
    """

    _SUPPORTED_TYPES = ('jpg')
    _UNSUPPORTED_TYPES = ('pdf', 'svg', 'ai', 'eps', 'dfx')
    _READ_MODES = ('rb', 'wb')

    def seek_str_treasure(image: str):
        """This method is used to extract string data from host image.

            :param image: host image path
            :param return: the str message

            How it works?
            ---------------
                (step 1) : open the host image in 'rb' mode.

                (step 2) : navigate to the end of the real jpg image. [ end point: hex(FF D9)]

                (step 3) : extract the string(treasure) in bytes and convert it to a string.

                (step 4) : returns the hidden string(treasure)
        """
        treasure_island_type = image.split('.')[-1]

        if treasure_island_type in EXPLORER._SUPPORTED_TYPES:
            with open(image, EXPLORER._READ_MODES[0]) as island:
                treasure_map = island.read()
                treasure_location = treasure_map.index(bytes.fromhex('FFD9'))
                island.seek(treasure_location + 2)
                treasure = f"{island.read()}".replace('b','')
 
                if len(treasure) == 2:
                    logging.error(f"*** No treasure hidden in {image} !!")
                else:
                    return treasure
        else:
            logging.error(f"*** currently .{treasure_island_type} images isn't supported as host image, Must be a .jpg !!")

    def seek_img_treasure(image: str, save=True, treasure_format='jpg'):
        """This method is used to extract hidden image from host image.

            :param image: host image 
            :param save: default(True)
                ** if true saves the hidden image in current working directory
                ** if false shows the hidden image without saving.
            :param treasure_format: defailt(jpg)
                ** saves the hidden file in provided format in treasure_format

            How it works?
            ---------------
                (step 1) : opens the host image in 'rb' mode.

                (step 2) : locate the hidden image in host image.

                (step 3) : convert the image in bytes array by calling BytesIO()

                (step 4) : save's or show the hidden image depending on save parameter
        """
        treasure_island_type = image.split('.')[-1]

        if treasure_island_type in EXPLORER._SUPPORTED_TYPES:
            if treasure_format in EXPLORER._UNSUPPORTED_TYPES:
                logging.error(f"*** currently {treasure_format} isn't supported !")
            else:
                with open(image, EXPLORER._READ_MODES[0]) as island:
                    treasure_map = island.read()
                    treasure_location = treasure_map.index(bytes.fromhex('FFD9'))
                    island.seek(treasure_location + 2)

                    if len(island.read()) == 0 :
                        logging.error(f"*** No treasure hidden in {image} !!")
                    else:
                        gold_coins = BytesIO(island.read())
                        if save:
                            treasure = Image.open(gold_coins)
                            treasure.save(f"treasure_from_({treasure_island_type})island.{treasure_format}")
                        else:
                            treasure = Image.open(gold_coins)
                            treasure.show()
        else:
            logging.error(f"*** currently .{treasure_island_type} images isn't supported as host image, Must be a .jpg !!")

    def seek_exe_treasure(image: str, treasure_name="treasure.exe"):
        """This method is used to extract hidden .exe files from host image.

            :param image: the host image path
            :param treasure_name: default(treasure.exe)

            How it works?
            ---------------
                (step 1) : opens the host image in 'rb' mode.

                (step 2) : locate the hidden exe file in host image.

                (step 3) : write the exe file bytes in a new(treasure_name) file.
        """
        treasure_island_type = image.split('.')[-1]

        if treasure_island_type in EXPLORER._UNSUPPORTED_TYPES:
            logging.error("*** currently {treasure_box_type} isn't supported !")
        else:
            if '.exe' in treasure_name:
                pass
            else:
                treasure_name = f"{treasure_name}.exe"
            with open(image, EXPLORER._READ_MODES[0]) as island:
                treasure_map = island.read()
                treasure_location = treasure_map.index(bytes.fromhex('FFD9'))
                island.seek(treasure_location + 2)

                gold_coins = island.read()

                if len(gold_coins) == 0:
                    logging.error(f"*** No treasure hidden in {image} !!")
                else:
                    with open(treasure_name, EXPLORER._READ_MODES[1]) as treasure:
                        treasure.write(gold_coins)

    def seek_file_treasure(image: str, treasure_name="treasure", treasure_format="text"):
        """This method is used to extract hidden .exe files from host image.

            :param image: the host image path.
            :param treasure_name: default(treasure)
                for saveing the file in user provided name.
            :param treasure_format: default(text)
                for saveing the file in user provided type.
                
            How it works?
            ---------------
                (step 1) : opens the host image in 'rb' mode.

                (step 2) : locate the hidden exe file in host image.

                (step 3) : write the exe file bytes in a new(treasure_name) file.
        """
        treasure_island_type = image.split('.')[-1]

        if treasure_island_type in EXPLORER._UNSUPPORTED_TYPES:
            logging.error("*** currently {treasure_box_type} isn't supported !")
        else:
            if treasure_format in treasure_name:
                pass
            else:
                treasure_name = f"{treasure_name}.{treasure_format}"

            with open(image, EXPLORER._READ_MODES[0]) as island:
                treasure_map = island.read()
                treasure_location = treasure_map.index(bytes.fromhex('FFD9'))
                island.seek(treasure_location + 2)

                gold_coins = island.read()

                if len(gold_coins) == 0:
                    logging.error(f"*** No treasure hidden in {image} !!")
                else:
                    with open(treasure_name, EXPLORER._READ_MODES[1]) as treasure:
                        treasure.write(gold_coins)


