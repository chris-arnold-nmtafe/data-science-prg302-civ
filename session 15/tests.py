import unittest
import wordle

class WordleTests(unittest.TestCase):
    def test_ok(self):
        #arrange
        guess = "hello"
        target = "hello"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(2,2,2,2,2))
    def test_not_ok(self):
        #arrange
        guess = "hello"
        target = "scram"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(0,0,0,0,0))

if __name__ == '__main__':
    unittest.main()
