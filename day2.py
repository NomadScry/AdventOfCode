rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
loss = 0
score = 0

# a = rock = x
# b = paper = y
# c = scissors = z

# rock beats scissors beats paper beats rock
with open('input2.txt') as file:
    fight = file.read()

fight = fight.split("\n")

for entry in fight:
    if entry == "A X": # rock v rock
        score += rock + draw
    elif entry == "A Y": # rock v paper
        score += paper + win
    elif entry == "A Z": # rock v scissors
        score += scissors + loss
    elif entry == "B X": # paper v rock
        score += rock + loss
    elif entry == "B Y": # paper v paper
        score += paper + draw
    elif entry == "B Z": # paper v scissors
        score += scissors + win
    elif entry == "C X":  # scissors v rock
        score += rock + win
    elif entry == "C Y": # scissors v paper
        score += paper + loss
    elif entry == "C Z": # scissors v scissors
        score += scissors + draw

print(f"The score is {score}.")
# x lose y draw z win
score = 0

for entry in fight:
    if entry == "A X": # rock v scissors lose
        score += loss + scissors
    elif entry == "A Y": # rock v rock draw
        score += draw + rock
    elif entry == "A Z": # rock v paper win
        score += win + paper
    elif entry == "B X": # paper v rock lose
        score += loss + rock
    elif entry == "B Y": # paper v paper draw
        score += draw + paper
    elif entry == "B Z": # paper v scissors win
        score += win + scissors
    elif entry == "C X":  # scissors v paper lose
        score += loss + paper
    elif entry == "C Y": # scissors v scissors draw
        score += draw + scissors
    elif entry == "C Z": # scissors v rock win
        score += win + rock

print(f"The score is {score}.")