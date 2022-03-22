import string
from random import randint

def random_user_id():
    chdg = string.ascii_letters + string.digits
    id = ''
    for i in range(6):
        ind = randint(0, (len(chdg)-1))
        id += chdg[ind]
    return id

print(random_user_id())

def user_id_gen_by_user():
    chdg = string.ascii_letters + string.digits
    ids = []
    length = input("Enter id length: ")
    mult = input("Enter how many ids: ")
    for i in range(int(mult)):
        id = ''
        for j in range(int(length)):
            ind = randint(0, (len(chdg)-1))
            id += chdg[ind]
        ids.append(id)
    return ids

print(user_id_gen_by_user())

def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return "rgb({},{},{})".format(r,g,b)

print(rgb_color_gen())
