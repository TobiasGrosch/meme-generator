"""A child class of the IngestorInterface to parse pdf files."""

import subprocess
import sys
import os

from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel


class PdfIngestor(IngestorInterface):
    """A child class of the IntestorInterface.

    Responsible for parsing pdf files.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod to check the file type and parse pdf files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type.')

        quotes = []

        try:
            subprocess.run(['pdftotext', path], stdout=subprocess.PIPE)
            txt_path = path[:-4] + '.txt'
            with open(txt_path, 'r') as infile:
                contents = infile.read()
        except OSError:
            print(f'Could not open/read file {path}.')

        for row in contents.split('\n')[0:-1]:
            if row != "":
                parsed = row.split('-')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        try:
            os.remove(txt_path)
        except OSError or FileNotFoundError:
            print(f'Could not delete temporary conversion file {txt_path}')
            sys.exit()

        return quotes
