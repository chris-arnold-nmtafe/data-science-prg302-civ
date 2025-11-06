import unittest
import wordle

class WordleTests(unittest.TestCase):
    def test_hello(self):
        #arrange
        guess = "hello"
        target = "hello"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(2,2,2,2,2))
    def test_scram(self):
        #arrange
        guess = "scram"
        target = "hello"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(0,0,0,0,0))
    def test_there(self):
        #arrange
        guess = "there"
        target = "hello"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(0,1,1,0,0))
    def test_shell(self):
        #arrange
        guess = "shell"
        target = "hello"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(0,1,1,2,1))
    def test_ollie(self):
        #arrange
        guess = "ollie"
        target = "hello"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(1,1,2,0,1))
    def test_lllll(self):
        #arrange
        guess = "lllll"
        target = "hello"
        #act
        result = wordle.score_guess(target,guess)
        #assert
        self.assertEqual(result,(0,0,2,2,0))

if __name__ == '__main__':
    unittest.main()
