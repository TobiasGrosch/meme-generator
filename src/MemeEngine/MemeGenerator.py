"""This module represents the Engine to create Memes."""

from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeEngine():
    """The MemeEngine creates the Memes based on input images and quotes."""

    def __init__(self, output_dir, file_ending='.png'):
        """Construct a MemeEngine based on an output directory and a file type.

        :param output_dir: A string for the output directory of the image.
        :param file_ending: A string for the image type, defaults to png.
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
            img = Image.open(img_path)
        except OSError:
            print(f'Could not open/read file {img_path}.')

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)

        draw.text((randint(5, width), randint(5, height)),
                  text+author, font=font, fill='white')

        out_path = self.output_dir + randint(0, 10000000) + self.file_ending
        img.save(out_path)

        return out_path
