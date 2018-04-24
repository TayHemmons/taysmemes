import string

letters = list(string.ascii_lowercase) # this makes a list of all letters from a-z
tstr = input('insert string: ') # string to check
outof = 0
for letter in letters:
    lcount = tstr.count(letter)
    if lcount > 0: # only count for letters which appear
        outof += 1
        print(letter + ': ' + str(lcount)) # how many times a certain letter appeared
print(str(outof) + '/26 letters used')
