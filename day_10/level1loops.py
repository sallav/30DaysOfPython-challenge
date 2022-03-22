
for i in range(11):
    print(i)

i=0
while i<11:
    print(i)
    i = i + 1

i = 10
while i>=0:
    print(i)
    i = i-1

for i in range(0, 10, -1):
    print(i)

hashes = '#######'

for i in range(8):
    print(hashes[0:i])

for i in range(8):
    k = ''
    for j in range(8):
        k = k + "# "    
    print(k)

for i in range(11):
    print('{} x {} = {}'.format(i,i,i*i))

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

for i in range(0, 101, 2):
    print(i)

for i in range(101):
    if i%2==0:
        continue
    print(i)


