import unittest
import playground.__main__ as filter_file


class TestFilter(unittest.TestCase):
    def setUp(self):
        self.filter = filter_file

    # def test_filter_main(self):
    #     self.assertEqual(self.filter.filter_main("я", "playground/test.txt"), "Здравствуйте!")

    def test_str_filter(self):
        with open("playground/test.txt", "r", encoding='utf-8') as file:
            self.assertEqual("".join(list(self.filter.str_filter("я", file))), "Здравствуйте!\n")


if __name__ == "__main__":
    unittest.main()
