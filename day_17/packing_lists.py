# Packing a list:

def list_args(*args):
    return list(args)

print(list_args(1,2,3,4,5))
print(list_args(1,2,3,4,5,6,7,8,9))

# Packing a dictionary:

def list_values(**kwargs):
    for key in kwargs:
        print(kwargs[key])
    return kwargs

print(list_values(name='Asabeneh', country='Finland', city='Helsinki', age=250))
print(list_values(one=1, two=2, three=3))