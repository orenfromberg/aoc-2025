total = 0

def stoi(s):
    acc = 0
    l = len(s)
    for i, n in enumerate(s):
        acc += int(n) * 10 ** (l-i-1)
    return acc

def itos(n):
    s = []
    while(n > 0):
        s.insert(0, str(n % 10))
        n //= 10
    return ''.join(s)

def is_invalid(n):
    # convert to string
    s = itos(n)
    l = len(s)
    if s[0:l//2] == s[l//2:]:
        return True
    return False

def get_sum_invalid_ids_in_range(r):
    if r == '':
        return 0

    total = 0
    first_str, last_str = r.split('-')
    # convert values to integers
    first = stoi(first_str)
    last = stoi(last_str)
    for n in range(first, last+1):
        if is_invalid(n):
            total += n
    return total


with open("input.txt", 'r') as file:
    for line in file:
        # Remove trailing whitespace/newline
        line = line.strip()
        
        ranges = line.split(',')

        for r in ranges:
            total += get_sum_invalid_ids_in_range(r)

    print(total)