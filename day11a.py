"""
2022 Advent of Code Day 11

Read in file input. Each monkey has items that can vary in worry. Each item is examined in turn, causing the worry to
increase before being divided by 3. Then the worry it tested and the item is moved accordingly. After a monkey has
examined each item, their turn ends and the next monkey takes their turn. After 20 turns, which two monkeys have
examined the most items? Report that as a multiple of the two inspection totals.
"""

with open("input11.txt") as file:
    file_input = file.read().splitlines()

empty = {
    "items": [],
    "operation": [],
    "test": 0,
    "true": 0,
    "false": 0,
    "inspections": 0,
}
id = -1
monkeys = []
for entry in file_input:
    entry = entry.strip()
    if entry.startswith("Monkey"):
        monkeys.append(empty.copy())
        id += 1
    elif entry.startswith("Starting"):
        monkeys[id]["items"] = [entry[16:]]
    elif entry.startswith("Operation"):
        monkeys[id]["operation"] = [entry[21:]]
    elif entry.startswith("Test"):
        monkeys[id]["test"] = int(entry[19:])
    elif entry.startswith("If true"):
        monkeys[id]["true"] = int(entry[25:])
    elif entry.startswith("If false"):
        monkeys[id]["false"] = int(entry[26:])

for pos, entry in enumerate(monkeys):
    for key, value in entry.items():
        if key == "items":
            temp = value[0]
            temp = temp.split(", ")
            monkeys[pos]["items"] = temp
        if key == "operation":
            temp = value[0]
            temp = temp.split()
            monkeys[pos]["operation"] = temp
    for key, value in entry.items():
        if key == "items":
            for loc, item in enumerate(value):
                monkeys[pos]["items"][loc] = int(item)

# Now that the data is massaged, start running it
rounds = 0
while rounds <= 19:
    for pos, entry in enumerate(monkeys):
        for key, value in entry.items():
            if key == "items":
                goto = 0
                toll = 0
                for loc, item in enumerate(value):
                    monkeys[pos]["inspections"] += 1
                    if monkeys[pos]["operation"][1] == "old":
                        operator = monkeys[pos]["items"][loc]
                    else:
                        operator = int(monkeys[pos]["operation"][1])
                    if monkeys[pos]["operation"][0] == "*":
                        monkeys[pos]["items"][loc] = (item * operator) // 3
                    elif monkeys[pos]["operation"][0] == "/":
                        monkeys[pos]["items"][loc] = (item / operator) // 3
                    elif monkeys[pos]["operation"][0] == "+":
                        monkeys[pos]["items"][loc] = (item + operator) // 3
                    elif monkeys[pos]["operation"][0] == "-":
                        monkeys[pos]["items"][loc] = (item - operator) // 3

                    if (monkeys[pos]["items"][loc] % monkeys[pos]["test"]) == 0:
                        goto = monkeys[pos]["true"]
                    else:
                        goto = monkeys[pos]["false"]
                    monkeys[goto]["items"].append(monkeys[pos]["items"][loc])
                    toll += 1
                for _ in range(toll):
                    monkeys[pos]["items"].pop(0)
    rounds += 1

in_order = []
for pos in range(len(monkeys)):
    in_order.append(monkeys[pos]["inspections"])
in_order.sort(reverse=True)
total = in_order[0] * in_order[1]
print(total)
