from tkinter import N


print(7//3 is int(2.7))

print(type('10') is type(10))

#print(int('9.8') is 10)

# rate per hour
hours = float(input('Enter hours: '))
rate = float(input('Enter rate per hour: '))
print('Your weekly earning is', rate*hours)

# seconds lived

years = int(input('Enter number of years you have lived: '))
seconds = 60 * 60 * 24 * 365 * years
print('You have lived for', seconds, 'seconds')

# table of numbers

table = ['1,1,1,1,1,', '2,1,2,4,8', '3,1,3,9,27', '4,1,4,16,64' , '5,1,5,25,125']
table = '\n'.join(table)
print(table)
