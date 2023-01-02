
with open('input8.txt') as file:
    file_input = file.read().strip()
# file_input is original, while square is side flipped. trees_seen is as described.
square = []
trees_seen = []
# removes the extraneous newlines
file_input = file_input.split('\n')
length = len(file_input)
# flip the square on it's side
for pos in range(length):
    square.append([])
    trees_seen.append([])
for entry in file_input:
    for pos, digit in enumerate(entry):
        square[pos].append(int(digit))
        trees_seen[pos].append(0)
# it's a given that the perimeter is all trees that can be seen
for i in range(length):
    for j in range(length):
        if i == 0:
            trees_seen[i][j] = 1
        elif i == length-1:
            trees_seen[i][j] = 1
        elif j == 0 or j == length-1:
            trees_seen[i][j] = 1
        else:
            continue
# check if trees can be seen from edge
# original input going left to right
for pos, entry in enumerate(file_input):
    tree_climber = 0
    for posj, digit in enumerate(entry):
        if int(digit) > tree_climber:
            tree_climber = int(digit)
            trees_seen[pos][posj] = 1
    tree_climber = 0
# original input going right to left
    for posj, digit in enumerate(reversed(entry)):
        if int(digit) > tree_climber:
            tree_climber = int(digit)
            trees_seen[pos][(length-1)-posj] = 2
# flipped input going left to right
for pos, entry in enumerate(square):
    tree_climber = 0
    for posj, digit in enumerate(entry):
        if digit > tree_climber:
            tree_climber = digit
            trees_seen[posj][pos] = 3
# and finally flipped input going right to left
    tree_climber = 0
    for posj, digit in enumerate(reversed(entry)):
        if digit > tree_climber:
            tree_climber = digit
            trees_seen[(length-1)-posj][pos] = 4
# count how many trees are seen
counter = 0
for entry in trees_seen:
    for digit in entry:
        if digit > 0:
            counter += 1
print("Trees seen:", counter)
#  reset trees_seen
for i in range(length):
    for j in range(length):
        trees_seen[i][j] = 0
# for each location of [x][y], if height is greater than height at [x+/-i][y] or if greater than [x][y+/-i] count that
# as a tree seen.
for x in range(length):
    for y in range(length):
        tree_climber = file_input[x][y]
        for i in range(length):
            if i <= y:
                continue
            # These are trees to the right
            if tree_climber > file_input[x][i]:
                trees_seen[x][y] += 1
            elif tree_climber <= file_input[x][i]:
                trees_seen[x][y] += 1
                break
    for y in range(length-1, -1, -1):
        temp_value = 0
        tree_climber = file_input[x][y]
        for i in range(length-1, -1, -1):
            if i >= y:
                continue
            # These are trees to the left
            if tree_climber > file_input[x][i]:
                temp_value += 1
            elif tree_climber <= file_input[x][i]:
                temp_value += 1
                break
        trees_seen[x][y] = trees_seen[x][y] * temp_value
for x in range(length):
    for y in range(length):
        temp_value = 0
        tree_climber = square[x][y]
        for i in range(length):
            if i <= y:
                continue
            # These are trees to the south
            if tree_climber > square[x][i]:
                temp_value += 1
            elif tree_climber <= square[x][i]:
                temp_value += 1
                break
        trees_seen[y][x] = trees_seen[y][x] * temp_value
    for y in range(length-1, -1, -1):
        temp_value = 0
        tree_climber = square[x][y]
        for i in range(length-1, -1, -1):
            if i >= y:
                continue
            # And these are trees to the north (up)
            if tree_climber > square[x][i]:
                temp_value += 1
            elif tree_climber <= square[x][i]:
                temp_value += 1
                break
        trees_seen[y][x] = trees_seen[y][x] * temp_value
biggest = 0
for x in range(length):
    for y in range(length):
        if trees_seen[x][y] > biggest:
            biggest = trees_seen[x][y]
print(biggest)
