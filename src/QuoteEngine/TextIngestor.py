"""A child class of the IngestorInterface to parse txt files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel


class TextIngestor(IngestorInterface):
    """A child class of the IntestorInterface for parsing txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod to check the file type and parse txt files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type.')

        quotes = []

        try:
            with open(path, 'r') as infile:
                contents = infile.read()
        except OSError:
            print(f'Could not open/read file {path}.')

        for row in contents.split('\n'):
            parsed = row.split('-')
            new_quote = QuoteModel(parsed[0], parsed[1])
            quotes.append(new_quote)

        return quotes
