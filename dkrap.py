#!/usr/bin/python3.5

import time

def d(x):
  time.sleep(x)


introLyrics=['so we\'re finally here','performing for you','if you know the words','you can join in too','put your hands together','if you want to clap','as we take you through','this monkey rap','HUH!']
chorusLyrics=['D','K','Donkey Kong','D','K','Donkey Kong is here']
dkLyrics=['he\'s the leader of the bunch','you know him well','he\'s finally here','to kick some tail','his coconut gun','fires in spurts','if he shoots ya','it\'s gonna hurt','he\'s bigger','faster','and stronger too','he\'s the first member','of the DK crew','HUH!']


def intro():
  for line in introLyrics:
    print(line)
    d(1)

def chorus():
  for line in chorusLyrics:
    print(line)
    d(1)

def dkVerse():
  for line in dkLyrics:
    print(line)
    d(1)


#intro()
#chorus()
dkVerse()
chorus()
