
with open('./input') as file:
    line = file.readline().rstrip()
    for i in range(len(line) - 3):
        part = line[i:i + 4]
        if len(set(part)) == len(part):
            print(i + 4)
            break
