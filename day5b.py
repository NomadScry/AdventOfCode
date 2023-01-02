# transfer stacks following instruction set then report what top cargo containers are

# set up stacks as lists
stack = ["ftclrpgq", "nqhwrfsj", "fbhwpmq", "vstdf", "qldwvfz", "zcls", "zbmvdf", "tjb", "qnbglsph"]

with open('input5.txt') as file:
    direction = file.read()

direction = direction.split('\n')

for line in direction:
    test = ''
    if line != '':
        test = line[0]
    if test == '[':
        continue
        # I have no idea how to strip and load the stack with the []s
    elif test == ' ':
        continue
    elif test == '':
        continue
    else:
        entry = line.split()
        howMany = int(entry[1])
        fromWhere = int(entry[3])-1
        toWhere = int(entry[5])-1
        # for x in range(howMany):
        intermediate = stack[fromWhere][-howMany:]
        stack[fromWhere] = stack[fromWhere][:-howMany]
        stack[toWhere] += intermediate

finalTops = ""
for entry in stack:
    finalTops = finalTops + entry[-1]
print(finalTops.upper())
