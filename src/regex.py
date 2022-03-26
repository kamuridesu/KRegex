# https://github.com/zeroone2numeral2/regex-bot/blob/ebb3a86795732485d41f103bd27cf0e1ac80d53b/bot/regexer.py#L19

import re


REGEX_FLAGS = "ilmsax"

FLAGS_DICT = {
    "i": re.I,
    "l": re.L,
    "m": re.M,
    "s": re.S,
    "a": re.A,
    "x": re.X
}

class Regex:
    def __init__(self, string, pattern, repl, flags=None):
        self.string = string
        self.pattern = pattern
        self.repl = repl
        self.count = 1  # by default, make just one replacement, unless the "g" flag is passed
        self.flags = 0  # default value for the "flags" argument of re.sub/re.subn

        if flags:
            for flag in flags:
                flag_lower = flag.lower()
                if flag_lower == "g":  # re.G: don't return after the first match
                    self.count = 0  # passing count=0 to resub/re.subn will make it not return after the first match
                if flag_lower in REGEX_FLAGS:
                    self.flags |= FLAGS_DICT[flag_lower]  # bitwise-concatenete the re.FLAG object

    def subn(self, escape_html=False):
        return re.subn(
            self.pattern,
            self.repl,
            self.string,
            flags=self.flags,
            count=self.count
        )

    def sub(self, escape_html=False):
        return re.sub(
            self.pattern,
            self.repl,
            self.string,
            flags=self.flags,
            count=self.count
        )
