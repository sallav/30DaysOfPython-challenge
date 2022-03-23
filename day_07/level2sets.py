A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

C = A.union(B)
print(C)
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B