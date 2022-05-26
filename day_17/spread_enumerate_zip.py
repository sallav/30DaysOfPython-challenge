# Spreading:

fruits = ['banana', 'lemon', 'apple']
vegs = ['carrot', 'cabbage', 'lettuce']

list_one = [*fruits, *vegs]

print(list_one)

# Enumerate:

for index, item in enumerate(fruits):
    print(index, item)

# Zip:

list_two = []

for f, v in zip(fruits, vegs):
    list_two.append((f, v))

print(list_two)