import ProgramModules.encrypt as encrypt
import ProgramModules.game as game
import unittest
import doctest




class Tests(unittest.TestCase):
    def test_random(self):
        random = encrypt.randint(100, 200)
        self.assertEqual(random, 500)
    def test_represent5(self):
        result = game.represents_int(5)
        self.assertEqual(result, True)
    def test_represent_word(self):
        result = game.represents_int("omg")
        self.assertEqual(result, False)

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(encrypt))
    tests.addTests(doctest.DocTestSuite(game))
    return tests

if __name__ == "__main__":
    doctest.testmod()
    unittest.main()