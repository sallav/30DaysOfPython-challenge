# Filter negative and zero using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_zero = [i for i in numbers if i<=0]

print(neg_zero)

# Flattening multidimensional list

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list = [num for row in [num for row in list_of_lists for num in row] for num in row]

print(list)

# list comprehension for tuples of powers

pows = [(i, pow(i, 0), pow(i, 1), pow(i, 2), pow(i, 3), pow(i, 4), pow(i, 5)) for i in range(10)]

print(pows)

# Flattening of list of lists

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

COUNTRIES = [[i[0], i[0][:3], i[1]] for i in [[val.upper() for val in b] for b in [val for b in countries for val in b]]]

Countries = [i for i in [val for val in [val for b in countries for val in b]]]

print(COUNTRIES)

print(Countries)