import cmath

def add_two_numbers(x, y):
    return x+y

print(add_two_numbers(2, 3))

def area_of_circle(r):
    return 3.14 * r * r

print(area_of_circle(10))

def add_all_nums(*nums):
    sum = 0
    for n in nums:
        if type(n)!=int and type(n)!=float:
            print('There was a non-number \'{}\' that was discarded'.format(n))
        else:
            sum += n
    return sum

print(add_all_nums(8, 7, 'Moi', 3.5, 10, 12))

def convert_celsius_to_fahrenheit(c):
    f = (c*9/5) +32
    return f

print('{} Fahrenheits'.format(convert_celsius_to_fahrenheit(20)))

def check_season(month):
    if month.startswith('December') or month.startswith('January') or month.startswith('February'):
        print('It\'s winter')
    if month.startswith('June') or month.startswith('July') or month.startswith('August'):
        print('It\'s summer')
    if month.startswith('March') or month.startswith('April') or month.startswith('May'):
        print('It\'s spring')
    if month.startswith('September') or month.startswith('October') or month.startswith('November'):
        print('It\'s autumn')

check_season('January')
check_season('May')

def calculate_slope(x1, x2, y1, y2):
    m = (y2-y1)/(x2-x1)
    return m

print(calculate_slope(3,6,2,-1))

def solve_quadratic_eqn(a, b, c):
#    eq = ax*x + bx + c
    hmm = (b*b) - (4*a*c)
    x1 = (-b + cmath.sqrt(hmm))/(2*a)
    x2 = (-b - cmath.sqrt(hmm))/(2*a)
    print(str(x1) + str(x2))

solve_quadratic_eqn(2, 5, 7)

def print_list(lst):
    for i in lst:
        print(i)

food = ['banana', 'potato', 'honey']
print_list(food)

def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1,-1,-1):
        rev.append(lst[i])
    return rev

print(reverse_list(food))

def capitalize_list_items(lst):
    cap = []
    for st in lst:
        st = st.capitalize()
        cap.append(st)
    return cap

print(capitalize_list_items(food))

def add_item(lst, item):
    lst.append(item)
    return lst

more_food = add_item(food, 'jam')
print(more_food)

def remove_item(lst, item):
    lst.remove(item)
    return lst

print(remove_item(more_food, 'honey'))

def sum_of_numbers(num):
    sum = 0
    for n in range(num+1):
        sum += n
    return sum

print(sum_of_numbers(5))

def sum_of_odds(num):
    sum = 0
    for n in range(num+1):
        if n%2!=0:
            sum += n
    return sum

def sum_of_evens(num):
    sum = 0
    for n in range(num+1):
        if n%2!=0:
            continue
        else:
            sum += n
    return sum

print(sum_of_evens(5))
print(sum_of_odds(5))