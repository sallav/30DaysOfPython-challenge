# Falsy statement
print(True is (len('python')<len('dragon')))

# True
print(('on' in 'python') and ('on' in 'dragon'))

print('jargon' in 'I hope this course is not full of jargon')

# False
print('on' not in 'python' and 'on' not in 'dragon')

# convert
print(str(float(len('python'))))

# even numbers
even = int(input('Give an even number:'))
print(even%2==0)