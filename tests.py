from main import RegexProcessor
import unittest


class TestRegexProcessor(unittest.TestCase):
    rgx = RegexProcessor("s/foo/bar/", "foo")
    rgx2 = RegexProcessor("s/foo/bar/g", "foo")
    
    def test_preprocess(self):
        self.assertEqual(self.rgx.preprocess(), ["foo", "bar", ""])
        self.assertEqual(self.rgx2.preprocess(), ["foo", "bar", "g"])

    def test_process(self):
        self.assertEqual(self.rgx.process(), "bar")
        self.assertEqual(self.rgx2.process(), "bar")


if __name__ == "__main__":
    unittest.main()
