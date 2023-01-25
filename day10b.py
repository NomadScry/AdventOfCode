"""
2022 Advent of Code Day 10 part 2
"""

with open('input10.txt') as file:
    file_input = file.read().strip().splitlines()

x = 1
cycles = 0
stepper = []
gross = 0
for entry in file_input:
    # noop instructions take a cycle but do not alter the value of x
    if entry.startswith('noop'):
        cycles += 1
        stepper.append([cycles, x])
    # addx instructions take two cycles to add a value to x
    else:
        # Split the entry to separate the value to add
        _ = entry.split()
        # the first cycle occurs but no change is made to value of x
        cycles += 1
        stepper.append([cycles, x])
        # the second cycle occurs BEFORE the new value is added to x
        cycles += 1
        stepper.append([cycles, x])
        x += int(_[1])

for i, j in stepper:
    # Takes the pixel location (i) and compares it to the sprite location (j)
    # If the sprite is within 3 of the pixel, a # is drawn. Otherwise, a . is drown
    # After 40 pixels are printed, the next line starts
    if (i-1)%40 == j or (i-1)%40 == j-1 or (i-1)%40 == j+1:
        print('#', end='')
    else:
        print('.', end='')
    if i % 40 == 0:
        print()
