def get_max_joltage(bank):
    max_joltage = 0
    for i, n in enumerate(bank):
        for m in bank[i+1:]:
            joltage = int(n) * 10 + int(m)
            max_joltage = max(max_joltage, joltage)
    return max_joltage

with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.strip()
    total += get_max_joltage(line)

print(total)
