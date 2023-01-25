# 2022 AdventOfCode Day 10
with open('input10.txt') as file:
    file_input = file.read().strip().splitlines()

# It's magic!
x = 1
cycles = 0
stepper = []
gross = 0
for entry in file_input:
    if entry.startswith('noop'):
        cycles += 1
        stepper.append([cycles, x])
    else:
        _ = entry.split()
        cycles += 1
        stepper.append([cycles, x])
        cycles += 1
        stepper.append([cycles, x])
        x += int(_[1])
for i, j in stepper:
    if i == 20:
        print(i*j)
        gross += (i*j)
    elif i == 60:
        print(i*j)
        gross += (i * j)
    elif i == 100:
        print(i*j)
        gross += (i * j)
    elif i == 140:
        print(i*j)
        gross += (i * j)
    elif i == 180:
        print(i*j)
        gross += (i * j)
    elif i == 220:
        print(i*j)
        gross += (i * j)

print(gross)
