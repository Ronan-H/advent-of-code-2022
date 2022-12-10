
def priority(supply):
    as_int = ord(supply)
    if as_int >= 97:
        return as_int - 97 + 1
    else:
        return as_int - 65 + 27

def calc_priority(bag):
    common = set(bag[:len(bag) // 2]) & set(bag[len(bag) // 2:])
    item = next(iter(common))
    return priority(item)

with open('./input') as file:
    print(sum(calc_priority(line.rstrip()) for line in file.readlines()))
