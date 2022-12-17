import copy
import numpy

# x, y
dir_map = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}

num_knots = 10
knots = [[0, 0] for i in range(num_knots)]
prev_knots = [[0, 0] for i in range(num_knots)]
head = knots[0]
tail = knots[-1]

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

            for k in range(1, len(knots)):
                knot = knots[k]
                parent = knots[k - 1]
                prev_parent = prev_knots[k - 1]

                diff = [parent[0] - knot[0], parent[1] - knot[1]]
                abs_diff = [abs(c) for c in diff]
                comp_min = min(abs_diff)
                comp_max = max(abs_diff)

                if comp_max > 1:
                    # knot isn't touching parent, it needs to move
                    knot[0] += numpy.clip(diff[0], -1, 1)
                    knot[1] += numpy.clip(diff[1], -1, 1)

            pos_tuple = (tail[0], tail[1])
            visited.add(pos_tuple)
            prev_knots = copy.deepcopy(knots)

print(len(visited))
