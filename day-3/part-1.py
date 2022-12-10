
def priority(supply):
    as_int = ord(supply)
    if as_int >= 97:
        return as_int - 97 + 1
    else:
        return as_int - 65 + 27

def calc_priority(bag):
    left_half = bag[:len(bag) // 2]
    right_half = bag[len(bag) // 2:]
    left_set = set(left_half)

    for supply in right_half:
        if supply in left_set:
            return priority(supply)

with open('./input') as file:
    print(sum(calc_priority(line.rstrip()) for line in file.readlines()))
