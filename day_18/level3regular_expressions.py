import re

# re.sub

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt):
    clean = re.sub(r'%|&|#|;|@', '', txt)
    cleaner = re.sub(r'\$', '', clean)
    return cleaner

cleaned_sentence = clean_text(sentence)

print(cleaned_sentence)

# Most frequent words

words = set(cleaned_sentence.split(' '))

counts = []

for word in words:
    all = re.findall('{}[^A-Za-z0-9]'.format(word), cleaned_sentence, re.I)
    counts.append((len(all), word))

counts.sort()
counts.reverse()

print(counts[0:3])