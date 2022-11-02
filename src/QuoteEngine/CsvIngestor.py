import pandas

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel

from typing import List

class CsvIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type.')

        quotes = []

        df = pandas.read_csv(path, header=0)

        for _, row in df.iterrows:
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes