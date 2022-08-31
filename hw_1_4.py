l1 = [10,2,3,4,89,78,89]
x = 25
newl1 = []

for l in l1:
    if l > x:
        newl1.append(l)

print(f'The original list is {l1}\n')
print(f'All the numbers greater than 25 are {newl1}')
