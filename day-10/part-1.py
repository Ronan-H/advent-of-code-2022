
lines = None
with open('./input') as file:
    lines = [line.rstrip() for line in file.readlines()]

def noop():
    pass

cycle = 1
x = 1
cur_op_type = None
cur_op_timer = 0
cur_op_action = noop

sum_cycles = set(i for i in range(20, 221, 40))
total = 0

# this block simulates 1 cycle on each iteration
while len(lines) > 0:
    if cur_op_timer == 0:
        # time to execute the current operation, and load the next one
        cur_op_action()

        line = lines.pop(0)
        parts = line.split()
        cur_op_type = parts[0]

        if cur_op_type == 'addx':
            def addx():
                global x
                x += int(parts[1])
            cur_op_action = addx
            cur_op_timer = 2
        else:
            # noop
            cur_op_action = noop
            cur_op_timer = 1

    # alternative: if 20 <= cycle <= 220 and (cycle - 20) % 40 == 0
    if cycle in sum_cycles:
        total += x * cycle

    cur_op_timer -= 1
    cycle += 1

print(total)

