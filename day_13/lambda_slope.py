# lambda to solve slope of linear functions

def calculate_slope(x1, x2, y1, y2):
    m = (y2-y1)/(x2-x1)
    return m


slope = lambda x1, x2, y1, y2: (y2-y1)/(x2-x1)

print(slope(2,4,6,3))