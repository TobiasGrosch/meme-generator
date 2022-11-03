"""A child class of the IngestorInterface to parse csv files."""

import pandas

from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel


class CsvIngestor(IngestorInterface):
    """A child class of the IntestorInterface.

    Responsible for parsing csv files.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod to check the file type and parse csv files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type.')

        quotes = []

        try:
            df = pandas.read_csv(path, header=0)
        except OSError:
            print(f'Could not open/read file {path}.')

        for _, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
