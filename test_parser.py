import unittest
from my_parser import Parser

my_parser = Parser()


class TestParser(unittest.TestCase): # aaa
    def setUp(self):
        self.path = 0
        self.url = 0
        self.domain = 0
        self.quality = 0

    def tearDown(self):
        pass

    def test_create_dir_of_group_type(self):
        self.assertRaises(TypeError, my_parser.create_dir_of_group, self.path)

    def test_create_dir_of_quality_type(self):
        self.assertRaises(TypeError, my_parser.create_dir_of_quality, self.path)

    def test_download(self):
        self.assertRaises(TypeError, my_parser.download, self, self.url, self.domain, self.quality)

    def test_get_memes(self):
        self.assertRaises(TypeError, my_parser.get_memes, self, self.domain)

    def test_API_conformity(self):
        self.assertEqual(my_parser.version, 5.21)


if __name__ == '__main__':
    unittest.main()
