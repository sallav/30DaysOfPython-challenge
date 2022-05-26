import re

 # valid python variables

def is_valid_variable(st):
    if re.match(r'\d', st):
        return False
    if re.search(r'-', st):
        return False
    return True

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True