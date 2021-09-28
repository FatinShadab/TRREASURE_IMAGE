import os
import glob
import logging
from PIL import Image


class GifMaker:
    """
    ABOUT:
    -------
        The GifMaker class is used to make gifs from images using Image module from pillow

    CONSTANT:
    ---------
        _UNSUPPORTED_TYPES: type --> tuple

    METHOD(s):
    ---------
        The methods of this class are:

            # make_gif --> Main method to genaret gif from images.
    """
    _UNSUPPORTED_TYPES = ('pdf', 'svg', 'ai', 'eps', 'dfx')
    def __init__(self, imgs_folder: str, image_formate: str, title: str, duration: int, loop: int, output_folder=os.getcwd(), optimize=False):
        """
        initializing the GifMaker class and store required data

        :param imgs_folder: path of folder which contains the images.
        :param Image_formate: filter to select images from imgs_folder like(JPG, PNG etc).
        :param title: title/name of the output gif.
        :param duration: duration of the gif image.
        :param loop:  loop images for given times.
        :param output_folder: folder path for saving output gif. (default: current working directory)
        :param optimize: to optimize the images. (default: False)
        """
        self.input_path = imgs_folder
        self.title = title
        self.duration = duration
        self.loop = int(abs(loop))
        self.optimize = optimize
        self.formate = image_formate.upper()
        # Prevent errors by wrong user input.
        self.imgs = glob.glob(f"{self.input_path}/*.{self.formate}") 
        if '\\' in output_folder[-1:]:
            self.output_path = output_folder
        else:
            self.output_path = f"{output_folder}\\"

    def make_gif(self):
        """ This method is used to genaret gifs

            How it works?
            -------------- 
                (step 1): It takes all provieded images from self.imgs
                and truns them to pillow Image objects and stored them
                in a list using list comprehension.

                (step 2): Than it save's all the image objects in the 
                1st image_object of the list with .gif exetension and given parameters.  
        """
        if self.formate.lower() in GifMaker._UNSUPPORTED_TYPES:
            logging.error(f"*** currently .{self.formate} images isn't supported !")
        else:
            if len(self.imgs) < 1:
                logging.error(f"Not enough images in {self.input_path}")
            else:
                # list comprehension
                image_objs = [Image.open(img) for img in self.imgs]

                # Save the gif
                image_objs[0].save(f'{self.output_path}{self.title}.gif', save_all=True, append_images=image_objs[1:], optimize=self.optimize, duration=self.duration, loop=self.loop)
