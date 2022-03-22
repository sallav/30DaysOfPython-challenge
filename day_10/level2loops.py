sum=0
for i in range(101):
    sum = sum + i
else: 
    print('The sum of all numbers is {}'.format(sum))

evens = 0
odds = 0

for i in range(101):
    if i%2!=0:
        odds = odds + i
    else:
        evens = evens + i
else:
    print('The sum of all evens is {}. The sum of all odds is {}.'.format(evens, odds))
    
