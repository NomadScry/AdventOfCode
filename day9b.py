# 2022 AdventOfCode Day 9
with open('input9.txt') as file:
    file_input = file.read().strip().splitlines()

tails = {0: [0,0], 1: [0,0], 2: [0,0], 3: [0,0], 4: [0,0], 5: [0,0], 6: [0,0], 7: [0,0], 8: [0,0], 9: [0,0]}
visited = []

for line in file_input:
    direction, distance = line.split()
    for steps in range(int(distance)):
        if direction =='R':
            tails[0][1] += 1
        elif direction == 'L':
            tails[0][1] -= 1
        elif direction == 'U':
            tails[0][0] += 1
        else:
            tails[0][0] -= 1

        for entry in range(0, 9, 1):
            if abs(tails[entry][0]-tails[entry+1][0]) + abs(tails[entry][1]-tails[entry+1][1]) > 2:
                if tails[entry][0]-tails[entry+1][0]>0:
                    tails[entry+1][0]+=1
                if tails[entry][0]-tails[entry+1][0]<0:
                    tails[entry+1][0]-=1
                if tails[entry][1]-tails[entry+1][1]>0:
                    tails[entry+1][1]+=1
                if tails[entry][1]-tails[entry+1][1]<0:
                    tails[entry+1][1]-=1
            if tails[entry][0] > tails[entry+1][0]+1:
                tails[entry+1][0] += 1
            elif tails[entry][0] < tails[entry+1][0]-1:
                tails[entry+1][0] -= 1
            if tails[entry][1] > tails[entry+1][1]+1:
                tails[entry+1][1] += 1
            elif tails[entry][1] < tails[entry+1][1]-1:
                tails[entry+1][1] -= 1

        if [tails[9][0], tails[9][1]] not in visited:
            visited.append([tails[9][0], tails[9][1]])

print(len(visited))
