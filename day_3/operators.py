# declaring variables
age = 100

height = 171.5

cmp = age * 0.5 * height

print(cmp)

# area of triangle
base = input('Enter base of the triangle: ')
height = input('Enter height of the triangle: ')
area = 0.5 * float(int(base)) * float(int(height))
print('The area of the triangle is', area)

# perimeter of triangle
side_a = input('Enter length of side a of triangle: ')
side_b = input('Enter length of side b of triangle: ')
side_c = input('Enter length of side c of triangle: ')
perim = float(side_a) + float(side_b) + float(side_c)
print('The perimeter of the triangle is', perim)

# rectangle area and perimeter
length = float(input('Enter length of the rectangle: '))
width = float(input('Enter width of the rectangle: '))
area = length * width
perim = 2*(length+width)
print('Perimeter is:', perim, 'Area is:', area)

# area and circumference of circle
pi = 3.14
radius = float(input('Enter radius of circle: '))
area = pi * radius * radius
circum = 2 * pi * radius
print('Area of the circle:', area, 'Circumference:', circum)
