def main():
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
    
    val = 50
    count = 0

    for line in lines:
        line = line.strip()
        if line:
            # Process each line here
            num = int(line[1:])

            if line[0] == 'R':
                val = (val + num) % 100
            else:
                val = (val + (100 - num)) % 100

            if val == 0:
                count += 1

    print(count)

if __name__ == "__main__":
    main()
