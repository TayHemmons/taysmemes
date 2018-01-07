#!/usr/bin/python3.5

import time

#use for delay between lines
def d(x):
  time.sleep(x)


introLyrics=['so they\'re finally here','performing for you','if you know the words','you can join in too','put your hands together','if you want to clap','as we take you through','this monkey rap','HUH!']
chorusLyrics=['D','K','Donkey Kong','D','K','Donkey Kong is here']
dkLyrics=['he\'s the leader of the bunch','you know him well','he\'s finally here','to kick some tail','his coconut gun','fires in spurts','if he shoots ya','it\'s gonna hurt','he\'s bigger','faster','and stronger too','he\'s the first member','of the DK crew','HUH!']
tinyLyrics=['this kong\'s got style','so listen up dudes','she can shrink in size','to suit her mood','she\'s quick and nimble','when she needs to be','she can float through the air','and climb up trees','if you choose her','you\'ll not choose wrong','with a skip and a hop','she\'s one cool kong','HUH!']
lankyLyrics=['he has no style','he has no grace','this kong has a funny face','he can handstand','when he needs to','and stretch his arms out','just for you','inflate himself','just like a balloon','this crazy kong','just digs this tune','HUH!']
diddyLyrics=['he\'s back again','and about time too','and this time','he\'s in the mood','he can fly real high with his jetpack on','with his pistols out','he\'s one tough kong','he\'ll make you smile','when he plays his tune','but kremlings beware','cause he\'s after you','HUH!']
chunkyLyrics=['finally','he\'s here for you','it\'s the last member','of the dk crew','this kong\'s so strong','it isn\'t funny','can make a kremling cry out','for his mummy','can pick up a boulder','with relative ease','makes crushing rocks','such a breeze','he may move slow','he can\'t jump high','but this kong\'s','one hell of a guy','HUH!']
outroLyrics=['walnuts','peanuts','pineapple smells','grapes','melons','oranges','and coconut shells']

def intro():
  for line in introLyrics:
    print(line)
    d(1)

def chorus():
  for line in chorusLyrics:
    print(line)
    if line == "D":
      d(.5)
    else:
      d(1)

def dkVerse():
  for line in dkLyrics:
    print(line)
    d(1)

def tinyVerse():
  for line in tinyLyrics:
    print(line)
    d(1)

def lankyVerse():
  for line in lankyLyrics:
    print(line)
    d(1)

def diddyVerse():
  for line in diddyLyrics:
    print(line)
    d(1)

def chunkyVerse():
  for line in chunkyLyrics:
    print(line)
    d(1)

fasterwords=['grapes','melons','oranges']

def outroVerse():
  for line in outroLyrics:
    print(line)
    if any(fasterword in line for fasterword in fasterwords):
      d(.5)
    else:
      d(1)


#play the song!
intro()
chorus()
dkVerse()
chorus()
tinyVerse()
chorus()
lankyVerse()
chorus()
diddyVerse()
chorus()
chunkyVerse()
chorus()
print('come on cranky, take it to the fridge') #im not writing a function for this one line
d(2)
outroVerse()
print('oh yeah')
d(1)
outroVerse()
