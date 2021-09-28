import logging
from io import BytesIO
from PIL import Image



class CONVERTER:
    """
        ABOUT:
        -------
        The CONVERTER class is used to convert files and images.

            *** currently vector graphics like(svg, ai etc) aren't supported !

        
        METHODS:
        ---------
            The methods of this class are:

            # convert_to_script: convert extracted programming script in text format
            to original script file.

            # convert_image:  convert images like (jpg <--> png, png <--> jfif, etc)
            *** currently vector graphics aren't supported !

    """
    _UNSUPPORTED_TYPES = ('pdf', 'svg', 'ai', 'eps', 'dfx')

    def convert_to_script(text_file: str, convert_to: str):
        """ This method is used to convert text files to script(.py, .cpp, .js etc)

            :param  text_file: the location/path of the target .text file
            :param  convert_to: output script name like (example.py)

            How it works?
            --------------
                (step 1): It opens the target text file in 'rb' mode 
                and reads the file

                (step 2): Than it creates and opens the file provieded in 
                convert_to parameter in 'wb' mode and write the target file
                in it. 
        """
        with open(text_file, 'rb') as island:
            gold_coins = island.read()

            with open (convert_to, 'wb') as treasure:
                treasure.write(gold_coins)

    def convert_image(target_image: str, format_to: str):
        """ This method is used to convert text files to script(.py, .cpp, .js etc)

            :param target_image: the path/location of the target image.
            :param format_to: the format(jpg, ong etc) to convert the target image.

            How it works?
            --------------
                (step 1): opens the target image in 'rb' mode.

                (step 2): transfroms the target image to byte array
                by calling BytesIo() method.

                (step 2): than it passes the image bytes array to the 
                Image.open() function

                (step 3): at the end it saves the image in the desired
                format stored in 'format_to' parameter by calling the
                Image.save() method.
        """ 
        target_image_name = target_image.split('.')[0]
        target_image_type = target_image.split('.')[1]

        format_to = format_to.lower()

        if format_to in CONVERTER._UNSUPPORTED_TYPES:
            logging.error(" *** currently vector graphics like(svg, ai etc) aren't supported !")

        if target_image_type in CONVERTER._UNSUPPORTED_TYPES:
            logging.error(" *** currently vector graphics like(svg, ai etc) aren't supported !")

        else:
            with open(target_image, 'rb') as f:
                img_bytes_arr = BytesIO(f.read())

                image = Image.open(img_bytes_arr)
                image.save(f"{target_image_name}.{format_to}")
