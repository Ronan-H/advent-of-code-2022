
crates = [
    'GTRW',
    'GCHPMSVW',
    'CLTSGM',
    'JHDMWRF',
    'PQLHSWFJ',
    'PJDNFMS',
    'ZBDFGCSJ',
    'RTB',
    'HNWLC'
]

crates = [[c for c in s] for s in crates]

with open('./input') as file:
    lines = [l.rstrip() for l in file.readlines()]
    lines = lines[10:]
    for line in lines:
        parts = line.split(' ')
        num_moving = int(parts[1])
        from_index = int(parts[3]) - 1
        to_index = int(parts[5]) - 1
        moving = crates[from_index][-num_moving:]
        crates[to_index] += moving[::-1]
        crates[from_index] = crates[from_index][:-num_moving]
    result = ''
    for c in crates:
        if len(c) > 0:
            result += c[-1]
    print(result)