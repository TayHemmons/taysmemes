import unittest
import pig

class pigtest(unittest.TestCase):

    def test_fixbasic(self):
        #turn a word that starts with one consonant into its pig latin form
        word = 'bridge'
        print('starting word: ' + word)
        pigword = pig.pigify(word)
        print('translated word: ' + pigword)
        self.assertEqual(pigword, 'ridgebay')

if __name__ == '__main__':
    unittest.main()
