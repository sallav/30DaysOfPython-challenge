
def is_prime(number):
    for n in range(number):
        if n==0 or n==1 or n==number:
            continue
        if number%n==0:
            return False
    return True

print(is_prime(7))
print(is_prime(4))
print(is_prime(19))

def uniq(lst):
    return len(lst)==len(set(lst))

l1 = [2, 4, 5, 4, 7]
l2 = [1, 3, 8, 5]

print(uniq(l1))
print(uniq(l2))

def sameType(lst):
    st = set()
    for i in lst:
        t = str(type(i))
        st.add(t)
    return len(st)==1

print(sameType(l1))

l3 = [1, 2, 4, 7, "Hi!"]

print(sameType(l3))

def valid(var):
    return var.isidentifier()

print(valid("4-Real"))

