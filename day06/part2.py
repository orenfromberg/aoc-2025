import math

with open('test.txt', 'r') as f:
    lines = f.readlines()

num_lines = len(lines)
num_chars = len(lines[num_lines-1])

matrix = [ [' '] * num_lines for _ in range(num_chars)]

for n in range(num_lines):
    for m in range(num_chars):
        matrix[m][n] = lines[n][m]

op = ''
terms = []
total = 0

# add an extra line at the bottom so it executes the last op
matrix.append([''])

for row in matrix:
    row = ''.join(row)
    is_empty = True if row.strip() == '' else False
    if is_empty:
        total += math.prod(terms) if op == '*' else sum(terms)
        terms = []
        continue
    if '*' in row:
        op = '*'
        row = row[0:-1]
    if '+' in row:
        op = '+'
        row = row[0:-1]
    val = int(''.join(row).strip())
    terms.append(val)

print(total)

