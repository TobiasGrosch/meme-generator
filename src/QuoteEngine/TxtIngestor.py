from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel

from typing import List

class TxtIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type.')

        quotes = []

        with open(path, 'r') as infile:
            contents = infile.read()

        for row in contents.split('\n'):
            parsed = row.split('-')
            new_quote = QuoteModel(parsed[0], parsed[1])
            quotes.append(new_quote)

        return quotes