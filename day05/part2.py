with open('input.txt', 'r') as f:
    lines = f.readlines()

ranges = []

for line in lines:
    line = line.strip()

    if '-' in line:
        ranges.append([int(c) for c in line.split('-')])
    
    elif line == '':
        break

# sort ranges
ranges.sort()

def intersects(r1, r2):
    if r1[0] <= r2[1]:
        return True
    return False

unioned_ranges = []

unioned_ranges.append(ranges[0])
ranges = ranges[1:]

for r in ranges:
    if intersects(r, unioned_ranges[-1]):
        unioned_ranges[-1][1] = max(unioned_ranges[-1][1],r[1])
    else:
        unioned_ranges.append(r)

print(unioned_ranges)

count = 0
for r in unioned_ranges:
    count += (r[1] - r[0] + 1)

print(count)