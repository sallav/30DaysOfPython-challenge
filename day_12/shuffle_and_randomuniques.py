from random import randint

def shuffle_list(lst):
    newlst = []
    length = len(lst)
    ord = list(range(length))
    for i in range(length):
        x = ord.pop(randint(0, (length-i-1)))
        newlst.append(lst[x])
    return newlst

l = ['hbd', 'bd', 'hi', 'cool', 'bye', 'xoxo', 'xxx', 'hello']

print(shuffle_list(l))

def unique_randoms():
    nums = []
    for i in range(7):
        num = randint(0,9)
        while num in nums:
            num = randint(0,9)
        nums.append(num)
    return nums

print(unique_randoms())