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
    print(entry)
    for digit in entry:
        if digit > 0:
            counter += 1
print("Trees seen:", counter)
