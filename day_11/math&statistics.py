import math

def evens_and_odds(number):
    evens = 0
    odds = 0
    for n in range(number):
        if n%2==0:
            evens += 1
        else:
            odds += 1
    return "Number of evens is {}, \nnumber of odds is {}.".format(evens, odds)

print(evens_and_odds(83))

def factorial(number):
    total = 1
    for n in range(number):
        if n==0:
            continue
        total = n*total
    return total*number

print(factorial(5))

def is_empty(param):
    if param:
        return False
    else:
        return True

print(is_empty(None))
print(is_empty([]))
print(is_empty([1, 2]))
print(is_empty(""))

def calculate_mean(params):
    sum = 0
    for n in params:
        sum += n
    return sum/len(params)

l1 = [2, 4, 3, 5, 1, 3, 8, 2, 2]
print(calculate_mean(l1))

def calculate_median(lst):
    m = int(len(lst)/2) 
    return sorted(lst)[m]

print(calculate_median(l1))

def calculate_mode(lst):
    s1 = set(lst)
    freq = 0
    mode = ""
    for n in s1:
        oc = lst.count(n)
        if oc>freq:
            freq = oc
            mode = n
    return mode

print(calculate_mode(l1))

def calculate_range(lst):
    return sorted(lst)[len(lst)-1]- sorted(lst)[0]

print(calculate_range(l1))

def calculate_variance(lst):
    sum = 0
    for i in lst:
        sqdiff = i - calculate_mean(lst)
        sum += sqdiff*sqdiff
    return sum/(len(lst)-1)

print(calculate_variance(l1))

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

print(calculate_std(l1))