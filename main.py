try:
    from src.regex import Regex
except Exception:
    from .src.regex import Regex


class RegexProcessor:
    """
    Class to process s/x/y/f into (x, y, f),
    readable by the custom Regex class.
    """
    def __init__(self, string: str, message: str):
        error = True
        if string.startswith("s"):
            if "/" in string:
                error = False
                self.string = string[2:]
        if error:
            raise ValueError("Invalid string: {}".format(string))
        self.message = message
    
    def preprocess(self):
        """
        Process the string and return a tuple of (pattern, repl, flags)
        """
        return self.string.split("/")

    def process(self):
        response = self.preprocess()
        if len(response) == 3:
            pattern, repl, flags = response
            return Regex(self.message, pattern, repl, flags).sub()
        elif len(response) == 2:
            pattern, repl = response
            return Regex(self.message, pattern, repl).sub()