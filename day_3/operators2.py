# slope, x-intercept and y-intercept
# y = 2*x - 2

x_inter = (0+2)/2
y_inter = 2*0 -2
slope = 2

print('In y=2x-2 x-intercept is', x_inter, 'y-intercept is', y_inter, 'and slope is', slope)

# slope and Euclidean distance
x1 = 2
y1 = 2

x2 = 6
y2 = 10

slope2 = y2-y1/x2-x1
dist = ((x1-x2)**2+(y1-y2)**2)**0.5
print('Euclidean distance between (2,2) and (6,10) is', str(dist)+',', 'the slope is', slope2)

# compare slopes
print('Slopes are equal?', slope==slope2)

# y = x^2 + 6x + 9
x = float(input('Give value of x:'))
y = x**2 + 6*x + 9 
print('y is', y)
print('Is y 0?', y==0)
