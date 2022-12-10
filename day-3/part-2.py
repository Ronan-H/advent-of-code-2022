
def priority(supply):
    as_int = ord(supply)
    if as_int >= 97:
        return as_int - 97 + 1
    else:
        return as_int - 65 + 27


with open('./input') as file:
    lines = [line.rstrip() for line in file.readlines()]
    badge_sum = 0
    for i in range(0, len(lines), 3):
        common = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
        item = next(iter(common))
        badge_sum += priority(item)

    print(badge_sum)
