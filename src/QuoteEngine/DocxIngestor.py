"""A child class of the IngestorInterface to parse docx files."""

from docx import Document
from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel


class DocxIngestor(IngestorInterface):
    """A child class of the IntestorInterface.

    Responsible for parsing docx files.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Classmethod to check the file type and parse docx files."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest this file type.')

        quotes = []

        try:
            doc = Document(path)
        except OSError:
            print(f'Could not open/read file {path}.')

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                parsed.strip()
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        return quotes
