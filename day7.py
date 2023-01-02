with open('input7.txt') as file:
    file_input = file.readlines()
dir_tree = {'/': [0]}
cd = ''
for entry in file_input:
    a = entry.split()
    if a[1] == 'cd':
        if a[2] == '/':
            cd = '/'
        elif a[2] == '..':
            last_slash = cd.rfind('/')
            cd = cd[:last_slash]
        else:
            if cd == '/':
                cd = cd + a[2]
            else:
                cd = cd + '/' + a[2]
            if cd not in dir_tree:
                dir_tree[cd] = [0]
    elif a[0] == 'dir':
        if cd == '/':
            dir_tree[cd].append(cd + a[1])
        else:
            dir_tree[cd].append(cd + '/' + a[1])
    elif a[0].startswith('$'):
        continue
    else:
        current_size = int(a[0]) + dir_tree[cd][0]
        dir_tree[cd][0] = current_size


def recaller(entry_):
    if type(entry_) is int:
        if key in sum_tree.keys():
            sum_tree[key] += entry_
        else:
            sum_tree[key] = entry_
    else:
        for inner_entry in dir_tree[entry_]:
            recaller(inner_entry)
    return

sum_tree = {}
for key, value in dir_tree.items():
    for entry in value:
        # call recaller
        recaller(entry)

gross = 0
for value in sum_tree.values():
    if value > 100000:
        continue
    else:
        gross += value
print(gross)
file_space = 70000000
avail = sum_tree['/']
needed = 30000000-(file_space-avail)
a = []
for value in sum_tree.values():
    if value >= needed:
        a.append(value)
a.sort()
print(a[0])