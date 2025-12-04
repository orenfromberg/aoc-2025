def has_fewer_than_4_adj(grid, row, col):
    num_adj = 0
    if grid[row-1][col-1] == "@":
        num_adj += 1
    if grid[row-1][col] == "@":
        num_adj += 1
    if grid[row-1][col+1] == "@":
        num_adj += 1
    if grid[row][col+1] == "@":
        num_adj += 1
    if grid[row+1][col+1] == "@":
        num_adj += 1
    if grid[row+1][col] == "@":
        num_adj += 1
    if grid[row+1][col-1] == "@":
        num_adj += 1
    if grid[row][col-1] == "@":
        num_adj += 1
    return num_adj < 4

with open('input.txt', 'r') as f:
    lines = f.readlines()

grid = []

for line in lines:
    line = line.strip()
    grid.append([c for c in line])

num_rows = len(grid)
num_cols = len(grid[0])

# pad grid with periods
for row in range(num_rows):
    grid[row].insert(0,'.')
    grid[row].append('.')
grid.insert(0, ['.' for _ in range(num_cols + 2) ])
grid.append(['.' for _ in range(num_cols + 2)])

total = 0

for row in range(1, num_rows+1):
    for col in range(1, num_cols+1):
        if grid[row][col] == '@' and has_fewer_than_4_adj(grid, row, col):
            total += 1

print(total)