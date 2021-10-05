class EnclosureException(Exception):
    """
    Exception raised when the a pair of enclosures doesn't match.
    For ex: "(something]" "(" does not mach "]"
    """

    def __init__(self, message, match):
        self.match = match
        self.message = message
        super().__init__(self.message, match)
