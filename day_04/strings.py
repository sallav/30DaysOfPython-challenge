
print('Thirty ' + 'Days ' + 'of ' + 'Python')

print('Coding ' + 'for ' + 'all')

company = 'Coding for All'
print(company)
print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:])

print(company.index('Coding'))
print(company.find('Coding'))

print(company.replace('Coding', 'Python'))

pyton = 'Python for everyone'
print(pyton.replace('everyone', 'All'))

print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

print(company[0])

print(len(company)-1)

print(company[10])

pytacr = ' '.join(pyton.split('ython'))
pytacr = ' '.join(pytacr.split('or'))
pytacr = ''.join(pytacr.split('veryone'))
pytacr = pytacr.replace(' ', '')
print(pytacr)

codacr = ' '.join(company.split('oding'))
codacr = ' '.join(codacr.split('or'))
codacr = ' '.join(codacr.split('ll'))
codacr = codacr.replace(' ', '').upper()
print(codacr)

print(company.index('C'))
print(company.index('f'))

cfap = "Coding for all people"
print(cfap.rfind('l'))

sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent.index('because'))

print(sent.rindex('because'))

print(sent[0:31] + sent[47:])

print(sent.find('because'))

print(company.startswith('Coding'))

print(company.endswith('Coding'))

trails = '   Coding For All      '
print(trails.strip('     ') + '?')
print(trails.strip('   '))

st1 = '30DaysOfPython'
st2 = 'thirty_days_of_python'
print(st1.isidentifier())
print(st2.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' #'.join(libraries))
print(' '.join(libraries))

sent2 = "I am enjoying this challenge.\nI just wonder what is next."
print(sent2)

tab1 = ['Name', 'Age', 'Country', 'City', 'Asabeneh', '250', 'Finland', 'Helsinki']
print('\t'.join(tab1))

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

num = 8
num2 = 6
print('{} + {} = {}'.format(num, num2, (num+num2)))
print('{} - {} = {}'.format(num, num2, (num-num2)))
st = '%d * %d = %d' %(num, num2, (num*num2))
print(st)
st ='%d / %d = %f' %(num, num2, (num/num2))
print(st)
print(f'{num} % {num2} = {(num%num2)}')
print(f'{num} // {num2} = {(num//num2)}')
print(f'{num} ** {num2} = {(num**num2)}')