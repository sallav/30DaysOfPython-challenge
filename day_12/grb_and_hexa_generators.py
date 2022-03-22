import colorsys
from random import randint

def list_of_hexa_colors(mult):
    colors = []
    hexa = '0123456789abcdef'
    for n in range(mult):
        color = '#'
        for i in range(6):
            color += hexa[randint(0, 15)]
        colors.append(color)
    return colors

print(list_of_hexa_colors(10))

def list_of_rgb_colors(mult):
    colors = []
    for n in range(mult):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        rgb = 'rgb({},{},{})'.format(r,g,b)
        colors.append(rgb)
    return colors

print(list_of_rgb_colors(20))

def generate_colors(type, mult):    # rgb or hexa colors
    colors = []
    hexa = '0123456789abcdef'
    if type is 'hexa':
        for i in range(mult):
            color = '#'
            for j in range(6):
                color += hexa[randint(0, 15)]
            colors.append(color)
    elif type is 'rgb':
        for i in range(mult):
            color = 'rgb({},{},{})'.format(randint(0,255),randint(0,255),randint(0,255))
            colors.append(color)
    return colors


print(generate_colors('hexa', 5))
print(generate_colors('rgb', 5))