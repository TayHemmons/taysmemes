import unittest
import pig

class pigtest(unittest.TestCase):

    def test_pigbasic(self):
        #turn a word that starts with one consonant into its pig latin form
        word = 'bridge'
        print('starting word: ' + word)
        pigword = pig.pigify(word)
        print('translated word: ' + pigword)
        self.assertEqual(pigword, 'ridgebay')

    def test_sentence(self):
        #turn multiple words into pig latin
        sentence = 'we need more food'
        print('starting sentence: ' + sentence)
        pigsentence = pig.pigsentence(sentence)
        print('translated sentence: ' + pigsentence)
        self.assertEqual(pigsentence, 'eway eednay oremay oodfay')



if __name__ == '__main__':
    unittest.main()
