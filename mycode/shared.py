import numpy as np

# configurations
lines = 5
columns = 50
timer = 15
gears = 5
car_number = 10
use_rule = True

# statistics
finished_cars = 0
forward_steps = 0
blocked_cars = 0
line_changes = 0
right_aligns = 0
clock_counter = 0

# cell[line][(timer, speed, line_is_changed)]
# timer - in how many time unit will change it position
# speed - how many time units takes a clock
# line_is_changed - it changed the line in the last clock
cells = np.zeros((lines, columns,), dtype=tuple)


def count_nonzero(line):
    return np.count_nonzero(cells[line])


def count_zero(line):
    return np.count_nonzero(cells[line] == 0)


def init_configuration():
    global cells
    global finished_cars
    global forward_steps
    global blocked_cars
    global line_changes
    global right_aligns
    global clock_counter
    cells = np.zeros((lines, columns,), dtype=tuple)
    finished_cars = 0
    forward_steps = 0
    blocked_cars = 0
    line_changes = 0
    right_aligns = 0
    clock_counter = 0


def print_statistics():
    print("Forward steps:{}".format(forward_steps))
    print("Blocked cars:{}".format(blocked_cars))
    print("Finished cars:{}".format(finished_cars))
    print("Total clocks:{}".format(clock_counter))
    print("Total line changes:{}".format(line_changes))
    print("Total right aligns:{}".format(right_aligns))
    if forward_steps + blocked_cars > 0:
        print("Total speed:{0:.3f}".format(forward_steps / (forward_steps + blocked_cars)))


def total_speed():
    if forward_steps + blocked_cars > 0:
        return forward_steps / (forward_steps + blocked_cars)
    return 0
