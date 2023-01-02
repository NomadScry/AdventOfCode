def evaluator(character):
    # a-z = 1 to 26
    # A-Z = 27 to 52
    if character.isupper():
        evalue = ord(character) - 38
    else:
        evalue = ord(character) - 96
    # print(character, evalue)
    return evalue


counter = 0

with open('input3.txt') as file:
    rucksacks = file.read()

rucksacks = rucksacks.split('\n')
# Take each line, split it in half, compare the sides to find the unequal, get value of it, and sum
for entry in rucksacks:
    x = (len(entry))
    x = x//2
    sideA = entry[0:x]
    sideB = entry[x:]
    for letter in sideA:
        if letter in sideB:
            counter += evaluator(letter)
            break

print(counter)

# chunk input by 3 lines, find shared character in all 3 lines, find value of badge, sum
someVariable = 0
counter = 0
while someVariable < len(rucksacks):
    for letter in rucksacks[someVariable]:
        if letter in rucksacks[someVariable+1] and letter in rucksacks[someVariable+2]:
            counter += evaluator(letter)
            break
    someVariable += 3

print(counter)
