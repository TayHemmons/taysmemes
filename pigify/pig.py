def pigify(word):
    word = list(word) # we need to make this a list to modify the contents
    firstletter = word[0] # grab first letter of word
    del word[0] # delete first letter of word
    word = ''.join(word) # make this a string again
    pigword = word + firstletter + 'ay'
    return pigword

def pigsentence(sentence):
    newsentence=[] # blank list for new sentence
    words = sentence.split() # split sentence into list
    for word in words: # for each word in the sentence, pigify
        newsentence.append(pigify(word))
    newsentence = ' '.join(newsentence) # turn list back into sentence
    return newsentence
