# -*- coding: utf-8 -*-
import re
import json

# Read file and count lines and words
# way 1

f = open('day_19/files/obama_speech.txt')
lines = f.readlines()
f.close()

wordcount = 0
for line in lines:
    words = line.split(' ')
    wordcount += len(words)

linecount = len(lines)
print('lines:', linecount)
print('words:', wordcount)

# way 2

f = open('day_19/files/michelle_obama_speech.txt', 'r')
lines = f.read().splitlines()
f.close()

wordcount = 0
for line in lines:
    words = line.split(' ')
    wordcount += len(words)

linecount = len(lines)
print('lines:', linecount)
print('words:', wordcount)

# way 3

with open('day_19/files/donald_speech.txt') as f:
    txt = f.read()

    words = txt.split(' ')
    wordcount = len(words)
    lines = re.findall('\n', txt)
    print('lines', len(lines)+1)
    print('words', len(words))

# way 4

with open('day_19/files/melina_trump_speech.txt') as f:
    linecount = wordcount = 0

    for line in f:
        linecount += 1
        words = line.split(' ')
        wordcount += len(words)
    
    print('lines', linecount)
    print('words', wordcount)

# read json file

with open('day_19/files/countries_data.json', encoding='latin1') as f:
    data = f.read()
    dctlist = json.loads(data)

    mostspoken = {}
    for dct in dctlist:
        for language in dct['languages']:
            if mostspoken.get(language) is None:
                mostspoken[language] = 1
            else:
                mostspoken[language] += 1

    tuplelist = mostspoken.items()
    ordered = sorted(tuplelist, key = lambda x: x[1], reverse=True) 
    print(ordered)   