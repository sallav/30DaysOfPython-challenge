age = [22, 19, 24, 25, 26, 24, 25, 24]

agest = set()
agest.update(age)

print('list length is ' + str(len(age)))
print('set length is ' + str(len(agest)))

# string is a sequence of characters, can be modified with functions and has indices

# list is an ordered collection, which can be modified

# tuple is an ordered collection, which cannot be modified after creation

# set is a collection of unique items with no duplicates. It is unordered and can be modified. 

str1 = 'I am a teacher and I love to inspire and teach people'
lst = str1.split()
print(lst)
print(len(lst))

st2 = set(lst)
print(st2)
print(len(st2))