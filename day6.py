'''
input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
twinput = "bvwbjplbgvbhsrlpgdmjqwftvncz"
triput = "nppdvjthqldpwncqszvftbrmjlhg"
quadput = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
quintput = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
'''

with open("input6.txt") as file:
    input = file.read()

for pos, entry in enumerate(input):
    str = input[pos:pos+14]
    if (str.count(entry) > 1) or (str.count(str[1]) > 1) or (str.count(str[2]) > 1) or (str.count(str[3]) > 1):
        continue
    elif (str.count(str[4]) > 1): continue
    elif (str.count(str[5]) > 1): continue
    elif (str.count(str[6]) > 1): continue
    elif (str.count(str[7]) > 1): continue
    elif (str.count(str[8]) > 1): continue
    elif (str.count(str[9]) > 1): continue
    elif (str.count(str[10]) > 1): continue
    elif (str.count(str[11]) > 1): continue
    elif (str.count(str[12]) > 1): continue
    elif (str.count(str[13]) > 1): continue
    else:
        print(pos+14, entry, str)
        break