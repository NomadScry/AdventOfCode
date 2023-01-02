counter = 0
overlap = 0

with open('input4.txt') as file:
    cleaningPairs = file.read()

cleaningPairs = cleaningPairs.split('\n')

for entry in cleaningPairs:
    a, b = entry.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    if b1 in range(a1, a2+1) and b2 in range(a1, a2+1):
        counter += 1
        # print(f'{a1}-{a2} {b1}-{b2} Inside A')
    elif a1 in range(b1, b2+1) and a2 in range(b1, b2+1):
        counter += 1
        # print(f'{a1}-{a2} {b1}-{b2} Inside B')

    if b1 in range(a1, a2+1) or b2 in range(a1, a2+1):
        overlap += 1
    elif a1 in range(b1, b2+1) or a2 in range(b1, b2+1):
        overlap +=1

print(counter)
print(overlap)