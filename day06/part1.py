with open('input.txt', 'r') as f:
    lines = f.readlines()

terms = []
ops = []
for line in lines:
    line = line.strip()
    if '*' in line or '+' in line:
        ops = line.split()
    else:
        terms.append([int(x) for x in line.split()])


print(terms)
print(ops)
num_ops = len(ops)
num_rows = len(terms)
total = 0
for i, op in enumerate(ops):
    if op == '*':
        product = 1
        for n in range(num_rows):
            product *= terms[n][i]
        total += product
    if op == "+":
        sum = 0
        for n in range(num_rows):
            sum += terms[n][i]
        total += sum
print(total)