
# x, y
dir_map = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}

head = [0, 0]
tail = [0, 0]

visited = set()

with open('./input') as file:
    for line in file:
        line = line.rstrip()

        dir_letter = line[0]
        vector = dir_map[dir_letter]
        mag = int(line[2:])

        for i in range(mag):
            head[0] += vector[0]
            head[1] += vector[1]
            diff = [head[0] - tail[0], head[1] - tail[1]]
            abs_diff = [abs(c) for c in diff]
            comp_min = min(abs_diff)
            comp_max = max(abs_diff)

            if comp_max > 1:
                # tail isn't touching head, it needs to move
                if comp_min == 1:
                    # diagonal move required
                    if abs(diff[0]) == 2:
                        tail[0] += diff[0] // 2
                        tail[1] += diff[1]
                    else:
                        tail[0] += diff[0]
                        tail[1] += diff[1] // 2
                else:
                    # lateral move required
                    if diff[0] != 0:
                        tail[0] += diff[0] // 2
                    else:
                        tail[1] += diff[1] // 2

            pos_tuple = (tail[0], tail[1])
            visited.add(pos_tuple)

            print(dir_letter, mag, 'V:', vector, 'H:', head, 'T:', tail, "CM:", comp_max)

print(len(visited))