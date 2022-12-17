import copy
import numpy

# x, y
dir_map = {
    'U': numpy.array((0, -1)),
    'R': numpy.array((1, 0)),
    'D': numpy.array((0, 1)),
    'L': numpy.array((-1, 0))
}

# My solution for part 2 allows part 1 to be solved just by setting num_knots to 2 here.
num_knots = 10
knots = numpy.array([[0, 0] for i in range(num_knots)])

visited = set()
lines = None

with open('./input') as file:
    lines = [line.rstrip() for line in file.readlines()]

for line in lines:
    dir_letter, mag = line[0], int(line[2:])
    head_vector = dir_map[dir_letter]

    for i in range(mag):
        knots[0] = numpy.add(knots[0], head_vector)

        for k in range(1, len(knots)):
            knot = knots[k]
            parent = knots[k - 1]

            diff = numpy.subtract(parent, knot)
            diff_abs = (abs(d) for d in diff)

            if max(diff_abs) > 1:
                # knot isn't touching parent, it needs to move
                knot_vector = [numpy.clip(d, -1, 1) for d in diff]
                knots[k] = numpy.add(knot, knot_vector)

        visited.add(tuple(knots[-1]))

print(len(visited))
