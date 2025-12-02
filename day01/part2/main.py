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
                for i in range(num):
                    val = (val + 1) % 100
                    if val == 0:
                        count += 1

            else:
                for i in range(num):
                    val -= 1
                    if val < 0:
                        val += 100
                    if val == 0:
                        count += 1

    print(count)

if __name__ == "__main__":
    main()
