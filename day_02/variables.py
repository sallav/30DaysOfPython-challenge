# Day 2: 30 Days of python programming

first_name = 'Salla'
last_name = 'Varkoi'
full_name = first_name + ' ' + last_name
country = 'Finland'
city = 'Vantaa'
age = '30'
year = '2022'
is_married = False
is_true = False
is_light_on = True
name, height, seriously = 'salla varkoi', 171, False

print(first_name, type(first_name))
print(last_name, type(last_name))
print(full_name, type(full_name))
print(country, type(country))
print(city, type(city))
print(age, type(age))
print(year, type(year))
print(is_married, type(is_married))
print(is_true, type(is_true))
print(is_light_on, type(is_light_on))
print(name, type(name))
print(height, type(height))
print(seriously, type(seriously))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one/num_two
remainder = num_one%num_two
exp = num_one ** num_two
floor_division = num_one//num_two

# area and circumference of a circle
radius = 30
pi = 3.14

area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius

radius = input('Give the radius of a circle: ')

area_of_circle = pi * (float(radius) ** 2)
print('The area of the circle is: ', area_of_circle)

# more user input

fist_name = input('What is your name? ')
last_name = input('What is your surename? ')
country = input('Where are you from? ')
age = input('How old are you? ')

print(first_name, last_name, 'from', country + ',', age, 'years old')

help('keywords')

