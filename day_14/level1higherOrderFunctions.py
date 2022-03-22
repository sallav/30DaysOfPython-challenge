from functools import reduce

# Built in higher order functions:

# The map function maps iterables, like a list, to another function given as a parameter, to use them as it's parameter one by one. Returns all results.

# The filter function goes through given iterables (such as a list) with the filtering function, given as a parameter. Which any item returns true on the calling function is returned, among the other iterables that satisfy criteria.

# The reduce function applies a given parameter function to iterables one by one, gathering all results to one returnable, reducing the given parameters to a single result.

# Differences:

# Higher order function is a function with other functions as parameters or returnables.

# Closure is a function with a nested function that can access the outer scope of the nesting function. The nested function is returned.

# Decorator is a function applied to a function. Decorator uses the other function as its parameter, manipulating it's return value and returning the result.


# Map:

def absolute(x):
    if x<0:
        return -x
    return x

lst = [2, -3, 0, 4, -11, 3]
lst2 = [8, 6, 3, 1, -2, -7]

absl = map(absolute, lst)

print(list(absl))

# Filter:

def negativeOrZero(x):
    if x<=0:
        return True
    return False

negZ = filter(negativeOrZero, lst)

print(list(negZ))

# Reduce:

def product(x, y):
    return x*y

prod = reduce(product, lst2)

print(prod)

# Higher order:

def printings(item):
    return print(item)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in countries:
    printings(item)

for item in names:
    printings(item)

for item in numbers:
    printings(item)