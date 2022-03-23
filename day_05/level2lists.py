
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(min(ages))
print(max(ages))

ages.append(min(ages))
ages.append(max(ages))

ages.sort()

median = (ages[int(len(ages)/2)] + ages[int((len(ages)/2))+1])/2
print(median)

sum = 0
for age in ages:
    sum += age
print(sum/len(ages))

range = max(ages)-min(ages)
print(range)

print(abs(range)==abs(min(ages)-max(ages)))