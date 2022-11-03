"""Main Ingestor class to encapsulate different ingestors.

In order to provide one interface to load any supported file type.
"""

from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel
from .DocxIngestor import DocxIngestor
from .CsvIngestor import CsvIngestor
from .TextIngestor import TextIngestor
# from .PdfIngestor import PdfIngestor


class Ingestor(IngestorInterface):
    """One common Interface for all ingestor child classes."""

    ingestors = [DocxIngestor, CsvIngestor, TextIngestor]
    # TODO add PdfIngestor

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """If ingestor is implemented for specific file type.

        The parser of the child class will be called.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
