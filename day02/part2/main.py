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
    s = itos(n)
    l = len(s)
    _set = set()
    for chunk_len in range(1,l//2+1):
        _set.clear()
        chunks = [s[i:i+chunk_len] for i in range(0, len(s), chunk_len)]
        for chunk in chunks:
            _set.add(chunk)
            if len(_set) > 1:
                break
        if len(_set) == 1:
            return True
    return False

def get_sum_invalid_ids_in_range(r):
    if r == '':
        return 0

    total = 0
    first_str, last_str = r.split('-')
    first = stoi(first_str)
    last = stoi(last_str)
    for n in range(first, last+1):
        if is_invalid(n):
            total += n
    return total


with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        
        ranges = line.split(',')

        for r in ranges:
            total += get_sum_invalid_ids_in_range(r)

    print(total)