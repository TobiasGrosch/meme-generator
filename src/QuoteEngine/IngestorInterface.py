"""Contains the abstract base class IngestorInterface.

This is defined by a classmethod 'can_ingest'.
'can_ingest' verifies if the file extension is supported by the system.

The abstractmethod 'parse' is responsible for outputting the content
into QuoteModel objects.
The specific parser for every file type is defined
in the respecitve modules.
"""

from abc import ABC, abstractmethod
from typing import List

from .Quote import QuoteModel


class IngestorInterface(ABC):
    """Abstract base clase for the Ingestor Interface."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify if the used file extension is supported by the system."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for parsing content into QuoteModel objects."""
        pass
