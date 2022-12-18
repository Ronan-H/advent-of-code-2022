
lines = None
with open('./input') as file:
    lines = [line.rstrip() for line in file.readlines()]

def noop():
    pass

screen_w, screen_h = 40, 6
screen_buffer = []

x = 1
cur_op_type = None
cur_op_timer = 0
cur_op_action = noop

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

    beam_pos = len(screen_buffer) % screen_w
    screen_buffer += '@' if beam_pos - 1 <= x <= beam_pos + 1 else ' '

    cur_op_timer -= 1

for h in range(screen_h):
    print(''.join(screen_buffer[h * screen_w:(h + 1) * screen_w]))
