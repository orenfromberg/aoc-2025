def get_max_joltage(bank):
    idx = 0
    _length = len(bank)
    vals = []
    for i in range(12):
        max_val = max(bank[idx:_length-12+i+1])
        vals.append(max_val)
        idx = bank[idx:].index(max_val) + idx + 1
    ret = sum([n * 10 ** (12 - i - 1) for i, n in enumerate(vals)])
    return ret

with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.strip()
    bank = [int(i) for i in line]
    total += get_max_joltage(bank)

print(total)
