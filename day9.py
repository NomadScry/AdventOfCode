# 2022 AdventOfCode Day 9
with open('input9.txt') as file:
    file_input = file.read().strip().splitlines()

head = [0, 0]
tail = [0, 0]
visited = []

for entry in file_input:
    direction, distance = entry.split()
    # print("==", direction, distance, "==")
    for steps in range(int(distance)):
        if direction == 'R':
            head[1] += 1
        elif direction == 'L':
            head[1] -= 1
        elif direction == 'U':
            head[0] += 1
        else:
            head[0] -= 1

        if abs(head[0] - tail[0]) + abs(head[1] - tail[1]) > 2:
            if head[0] - tail[0] > 0:
                tail[0] += 1
            if head[0] - tail[0] < 0:
                tail[0] -= 1
            if head[1] - tail[1] > 0:
                tail[1] += 1
            if head[1] - tail[1] < 0:
                tail[1] -= 1

        if head[0] > tail[0]+1:
            tail[0] += 1
        elif head[0] < tail[0]-1:
            tail[0] -= 1
        if head[1] > tail[1]+1:
            tail[1] += 1
        elif head[1] < tail[1]-1:
            tail[1] -= 1

        if [tail[0], tail[1]] not in visited:
            visited.append([tail[0], tail[1]])
        
        """
        for i in range(5, -1, -1):
            for j in range(6):
                if head[0] == i and head[1] == j:
                    print("H", end=' ')
                elif tail[0] == i and tail[1] == j:
                    print("T", end=' ')
                else:
                    print(".", end=' ')
            print()
        print()
        """
print(len(visited))
