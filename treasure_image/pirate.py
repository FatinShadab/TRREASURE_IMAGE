import logging
from io import BytesIO
from PIL import Image


class PIRATE:
    """
    ABOUT:
    --------
        The PIRATE class is used to hide(append) data to a jpg Image.
         
        files that can be hide: 
            # strings
            # files
                # All type
            # images
                # All Type(vactor graphics aren't supported in this release)

    CONSTANT:
    ---------
            _WRITE_MODES: type --> tuple
            _SUPPORTED_TYPES: type --> tuple 
            _UNSUPPORTED_TYPES: type --> tuple

    METHODS:
    --------
        The methods of this class are:

          # hide_str_treasure --> hide string in image
          # hide_img_treasure --> hide image in other image
          # hide_file_treasure --> hide files in image
    """
    # Global  CONSTANT variable
    _WRITE_MODES = ('ab', 'rb')
    _SUPPORTED_TYPES = ('jpg')
    _UNSUPPORTED_TYPES = ('pdf', 'svg', 'ai', 'eps', 'dfx', 'jfif')
    

    def hide_str_treasure(image: str, treasure: str):
        """ This method is used to hide string data in host image.

            :param image: The name of the host image (must be a .jpg image)
            :param treasure: The str which will be hidden 

            How it works?
            ---------------
            *** if self.treasure is a str than -->

                    (step 1) : this method takes the string, saved in self.treasure
                    and covert it to bytes 

                    (step 2) : than appends the bytes at the 
                    end of the jpeg image hex (FF D9)
            
            *** if self.treasure is a list or tuple than -->
                    (step 1) : this method takes the self.treasure(list/tuple)
                    and join the elements in one sting by newline

                    (step 2) : than covert it to bytes than appends the bytes at the 
                    end of the jpeg image hex (FF D9) 

                    *** This should be used when user tries to hide 
                    a message of more than one line ***
        """
        treasure_box_type = image.split('.')[-1] # image type extentions like (.jpg, .png etc)

        if treasure_box_type in PIRATE._SUPPORTED_TYPES:
            if type(treasure) is str:
                treasure = treasure

            if type(treasure) is list or type(treasure) is tuple:
                treasure = '\n'.join(treasure)

            with open(image, PIRATE._WRITE_MODES[0]) as box:
                box.write(bytes(treasure, 'utf-8'))
        else:
            logging.error(f"*** currently .{treasure_box_type} images isn't supported as host image, Must be a .jpg !!")

    def hide_img_treasure(image: str, treasure: str):
        """This method is used to hide image(type=all) in host image(type=jpg).

            :param image: The name of the host image (must be a .jpg image)
            :param treasure: The img which will be hidden 

            How it works?
            ---------------
                (step 1) : this method takes the treasure(image) and open's
                it with Image.open() method from pillow.
                
                (step 2) : than by BytesIO() method from io,
                we crated the image byte array.
                
                (step 3) : After that by calling save() we saved the image stored 
                in treasure in the byte array in it's original format.

                (step 4) : Finally we append the image bytes in the host image 
        """
        treasure_box_type = image.split('.')[-1] # image type extentions like (.jpg, .png etc)
        treasure_type = treasure.split('.')[-1] # for file type extentions like (.exe, .py etc)

        if treasure_box_type in PIRATE._SUPPORTED_TYPES: #or treasure_type in PIRATE._UNSUPPORTED_TYPES:
            if treasure_type in PIRATE._UNSUPPORTED_TYPES:
                logging.error(f"*** currently .{treasure_type} images isn't supported as treasure!")
            else:
                treasure = Image.open(treasure)
                gold_coins_arr = BytesIO()
                treasure.save(gold_coins_arr, format=treasure_type)

                with open(image, PIRATE._WRITE_MODES[0]) as box:
                    box.write(gold_coins_arr.getvalue())
        else:
            logging.error(f"*** currently .{treasure_box_type} isn't supported as host image, Must be .jpg !!")

    def hide_file_treasure(image: str, treasure: str):
        """his method is used to hide files(type=all) in host image(type=jpg).

            
            :param image: The name of the host image (must be a .jpg image)
            :param treasure: The file which will be hidden 

            How it works?
            ---------------
                (step 1) : it takes the host image and open it in 'ab' mode.

                (setp 2) : than it opens the give file in 'rb' mode.

                (step 2) : At the end the given file is append to the
                host image by calling write() and read() methods.
        """
        treasure_box_type = image.split('.')[-1] # image type extentions like (.jpg, .png etc)
            
        if treasure_box_type in PIRATE._SUPPORTED_TYPES:
            
            with open(image, PIRATE._WRITE_MODES[0]) as box, open(treasure, PIRATE._WRITE_MODES[1]) as gold_coins:
                box.write(gold_coins.read())
        else:
            logging.error(f"*** currently .{treasure_box_type} images isn't supported as host image, Must be a .jpg !!")

