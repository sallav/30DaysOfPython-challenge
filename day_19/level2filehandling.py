import re

# Extract email addresses

with open('day_19/files/email_exchanges_big.txt') as f:
    all = []
    for line in f:
        addresses = re.findall('[a-z0-9\.]+@[a-z0-9\.]+\.[a-z\.]+', line)
        all.extend(addresses)
    print(all)

# Most common words

def find_most_common_words(textfile, amount):
    f = open(textfile)
    text = f.read()
    f.close()
    text = text.lower()
    wordlist = re.findall('[a-z\']+', text, re.I)
    words = set(wordlist)
    appearance = []
    for word in words:
        count = 0
        for w in wordlist:
            if w==word:
                count += 1
        appearance.append((count, word))
    appearance.sort(reverse=True)
    return appearance[:amount]

print('Donald', find_most_common_words('day_19/files/donald_speech.txt', 40))
print('Obama', find_most_common_words('day_19/files/obama_speech.txt', 40))
print('Michelle', find_most_common_words('day_19/files/michelle_obama_speech.txt', 40))
print('Melina', find_most_common_words('day_19/files/melina_trump_speech.txt', 40))
