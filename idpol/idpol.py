#!/usr/bin/python3.7

def ltor(words):
    return words.replace('l','r')

def ruleset1(words):
    words = words.replace('ie','ee')
    words = words.replace('ble','bur')
    return words

def ruleset2(words):
    # all full word replace
    words = words.replace('the','da')
    return words

def dumpling(words):
    words = ruleset1(words)
    words = ltor(words)
    return words