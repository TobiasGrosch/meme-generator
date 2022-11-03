"""Represents the model for Quotes.
   Quotes exist out of a body and an author.
"""

class QuoteModel():
    """QuoteModel Class defines that a Quote exists our of a body and an author."""
    def __init__(self, body: str, author: str) -> None:
        """Constructs a QuoteModel based on a body and an author.
        
        :param body: A string containing the quote.
        :param author: A string containing the name of the author.
        """
        self.body = body
        self.author = author
    
    def __str__(self):
        """Return 'str(self)', a human readable represenation of a quote."""
        return f'"{self.body}" - {self.author}'