# Meme-Generator


## Introduction

The Meme-Generator is an application to generate dynamically Memes based on an image with an overlaid quote. 

The quote content can be provided in various file types. Currently the QuoteEngine supports txt, docx, csv and pdf as input file types.

Beside the automatic mode to generate random Memes, the user can also manually input an image and it's quote to get the custom Meme generated.

The application can be used via command line and as a web service.

-----

## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── .gitignore
  ├── requirements.txt *** The dependencies you need to install with "pip3 install -r requirements.txt"
  └── src
      ├── _data 
      |   ├── DogQuotes *** Dog quotes in csv, docx, pdf and txt format
      |   ├── photos/dog *** Example images of dogs in jpg format
      |   └── SimpleLines *** Generic quotes in csv, docx, pdf and txt format
      ├── MemeEngine
      |   ├── __init__.py
      |   └── MemeGenerator.py *** This module represents the Engine to create Memes
      ├── QuoteEngine
      |   ├── __init__.py
      |   ├── CsvIngestor.py *** A child class of the IngestorInterface to parse csv files
      |   ├── DocxIngestor.py *** A child class of the IngestorInterface to parse docx files
      |   ├── Ingestor.py *** Main Ingestor class to encapsulate different ingestors
      |   ├── IngestorInteface.py *** Contains the abstract base class IngestorInterface
      |   ├── PdfIngestor.py *** A child class of the IngestorInterface to parse pdf files
      |   ├── Quote.py *** Represents the model for Quotes
      |   └── TextIngestor.py *** A child class of the IngestorInterface to parse txt files
      ├── templates *** Front-end html templates
      ├── app.py *** Contains the flask server implementation
      └── meme.py *** Generates the meme and is the main script to be executed for command line usage
  ```
-----
## How to use Meme Generator locally

1. **Install the dependencies:**
```
pip install -r requirements.txt
```
The open source XpdfReader utility is used to convert the pdf content to text.
For furhter information check this page: [XpdfReader](https://www.xpdfreader.com/pdftotext-man.html)

Since the `apt-get`installation method for Ubuntu20.4 of Xpdf is not supported anymore, I recommend to use Homebrew.
Install Homebrew with the instructions provided [here](https://brew.sh/) and add it to your PATH (details provided at the end of installation process in terminal output).

Once Homebrow is installed, simply run `brew install xpdf` in your terminal.

2. **Change directory:**
First make sure to change directory from root folder to source folder:
```
cd ./src
```

3. **Option 1: Run the application with Web server:**
```
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 app.py
```

4. **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

5. **Option 2: Use the Meme Generator as CLI application:**<br>
Image path, the quote body and the author are optional parameters.
```
python3 meme.py --path {image_path} --body {quote_body} -- author {quote_author}
```