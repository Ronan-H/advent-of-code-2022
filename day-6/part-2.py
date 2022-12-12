
with open('./input') as file:
    line = file.readline().rstrip()
    for i in range(len(line) - 13):
        part = line[i:i + 14]
        if len(set(part)) == len(part):
            print(i + 14)
            break
