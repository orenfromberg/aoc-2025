with open('input.txt', 'r') as f:
    lines = f.readlines()

ranges = []

ids = []

for line in lines:
    line = line.strip()

    if '-' in line:
        ranges.append([int(c) for c in line.split('-')])
    
    elif line == '':
        continue

    else:
        ids.append(int(line))

count = 0
for id in ids:
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            count += 1
            break

print(count)