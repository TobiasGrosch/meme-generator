import random
import os
import sys
import requests

from flask import Flask, render_template, request

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   #'./_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]


    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form['image_url']
    image_extension = image_url.split('.')[-1]
    body = request.form['body']
    author = request.form['author']

    response = requests.get(image_url)

    temp_dir = './tmp/'
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    temp_img_path = temp_dir + 'temp_image.' + image_extension

    with open(temp_img_path, 'wb') as image:
        image.write(response.content)

    meme.file_ending= ('.' + image_extension)
    path = meme.make_meme(temp_img_path, body, author)

    try:
        os.remove(temp_img_path)
    except OSError or FileNotFoundError:
        print(f'Could not delete temporary file {temp_img_path}')
        sys.exit()

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
