#!/usr/bin/python3.7

def ltor(words):
    return words.replace('l','r')

def ruleset1(words):
    newsentence = []
    words = words.replace('.','')
    words = words.rstrip()
    for word in words.split(' '):
        if word != 'die':
            word = word.replace('ie','ee')
        word = word.replace('ble','bur')
        word = word.replace('tle','tur')
        if word == 'the': # this one is a full word replace
            word = word.replace('the','da')
        newsentence.append(word)
        words = reconstruct(newsentence)
    return words

def reconstruct(wordlist): # takes a list and turns it into a string
    sentence = ''
    for word in wordlist:
        sentence = sentence + ' ' + word
    sentence = sentence + '.'
    return sentence

def dumpling(words):
    words = ruleset1(words)
    words = ltor(words)
    return words