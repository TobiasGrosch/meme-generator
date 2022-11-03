"""This module represents the Engine to create Memes."""

import sys
import os

from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeEngine():
    """The MemeEngine creates the Memes based on input images and quotes."""

    def __init__(self, output_dir, file_ending='.jpg'):
        """Construct a MemeEngine based on an output directory and a file type.

        :param output_dir: A string for the output directory of the image.
        :param file_ending: A string for the image type, defaults to jpg.
        """
        self.output_dir = output_dir
        self.file_ending = file_ending

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Meme with a text and author written in the meme.

        :para img_path: A string containing the path to the local image.
        :para text: A string containing the quote written on the image.
        :para author: A string containing the author's name.
        :para width: An integer for the Meme's width, defaulting to 500.
        """
        try:
            with Image.open(img_path) as img:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./templates/arial.ttf', size=20)

                draw.text((randint(5, 50), randint(5, height-20)),
                        text + ' - ' + author, font=font, fill='white')

                out_path = self.output_dir + '/' +str(randint(0, 10000000)) + self.file_ending

                if not os.path.exists(self.output_dir):
                    os.mkdir(self.output_dir)

                img.save(out_path)
        except OSError or FileNotFoundError:
            print(f'Could not open/read file {img_path}')
            sys.exit()

        return out_path
