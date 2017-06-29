import averages_files.averages as averages
import averages_files.get_data as get_data
import unittest
import doctest


class Tests(unittest.TestCase):
    def test_arithmetic(self):
        result = averages.arithmetic((1, 2, 3), (1, 1, 1))
        self.assertEqual(result, 2)
    def test_geometric(self):
        result = averages.geometric((1, 9), (1, 1))
        self.assertEqual(result, 3)
    def test_harmonic(self):
        result = averages.harmonic((2, 4, 4), (1, 1, 1))
        self.assertEqual(result, 3)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(averages))
    tests.addTests(doctest.DocTestSuite(get_data))
    return tests


if __name__ == "__main__":
    doctest.testmod()
    unittest.main()