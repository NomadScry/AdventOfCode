with open('input.txt') as file:
    calorie_input = file.read()

elf = 0
calories = [0]
calorie_list = calorie_input.split("\n")

for entry in calorie_list:
    if entry == "":
        elf = elf + 1
        calories.append(0)
    else:
        calories[elf] += int(entry)

calories.sort(reverse=True)

hungry_elves = calories[0] + calories[1] + calories[2]
print(hungry_elves)