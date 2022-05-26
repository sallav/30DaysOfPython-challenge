import re

# re.findall

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = paragraph.split(' ')

count = 0
freq = ''
for word in words:
    all = re.findall('{}[^A-Za-z0-9]'.format(word), paragraph, re.I)
    print(all)
    if len(all)>count:
        count = len(all)
        freq = word

print("Most frequent", freq, "found", count, "times")

# re.findall regular expressions

p2 = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

regex = r'-?\d+'
positions = re.findall(regex, p2)
positionints = []
for p in positions:
    positionints.append(int(p))

positionints.sort()

distance = (positionints[len(positionints)-1]) - positionints[0] 

print(positionints)
print(distance)