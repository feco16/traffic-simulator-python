import numpy as np

import shared

map_data = cells = np.zeros((shared.lines, shared.columns), dtype=tuple)

number = 3

collision = None
collisions = {"UP": (0, 1), "DOWN": (shared.lines - 1, 1), "LEFT": (1, 0),
              "RIGHT": (1, shared.columns - 1)}

default_positions = {"UP": (1, None), "DOWN": (shared.lines - 2, None), "LEFT": (None, 1),
                     "RIGHT": (None, shared.columns - 2)}

obstacles = (
    ((50, 50), (70, 50)),
    ((50, 50), (200, 100)),
    ((50, 52), (200, 102)),
    ((70, 72), (100, 102)),
    ((270, 72), (160, 102)),

)


def create_map():
    """ Create the initial map. """
    for line in range(0, shared.lines - shared.handle_altitude):
        map_data[line][0] = (1, -1)
        map_data[line][shared.columns - 1] = (1, -1)

    for column in range(0, shared.columns):
        map_data[0, column] = (-1, 1)
        if column <= shared.left_space or column > shared.columns - shared.left_space:
            map_data[shared.lines - 1, column] = (-1, 1)

    for obs in obstacles:
        for line, column in get_line_between_points(obs[0], obs[1]):
            map_data[line, column] = (1, -1)


def get_line_between_points(A, B, multiply = 1):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    m = (y1 - y2) / (x1 - x2) if x1 != x2 else 0
    b = (x1 * y2 - x2 * y1) / (x1 - x2)

    y = [(int(x), int(m * x + b)) for x in np.arange(x1, x2 + (1 if x2 > 0 else -1),
                                                     (1 if x2 > 1 else -1 )/ multiply)]
    print("Calculated line: {}".format(y))
    return y


def move_ball():
    """ Move ball position according to the current direction"""
    print("Current position: ({},{}). "
          "Direction: ({},{}). Value: {}".format(shared.ball_yy, shared.ball_xx,
                                                 shared.direction[0], shared.direction[1],
                                                 map_data[shared.ball_yy][shared.ball_xx]))
    if does_apply_direction():
        shared.ball_yy += shared.direction[0]
        shared.ball_xx += shared.direction[1]
    else:
        pass
        # shared.ball_yy = shared.ball_yy + shared.direction[0] \
        #     if default_positions.get(collision)[0] == None else default_positions.get(collision)[0]
        # shared.ball_xx = shared.ball_xx + shared.direction[1] \
        #     if default_positions.get(collision)[1] == None else default_positions.get(collision)[1]


def handles():
    pass


def does_apply_direction():
    global collision
    collision = None
    # if shared.direction[0] < 0 and shared.ball_yy <= abs(shared.direction[0]):
    #     collision = "UP"
    # if shared.ball_yy > shared.lines - shared.direction[0] - 1:
    #     collision = "DOWN"
    # if shared.direction[1] < 0 and shared.ball_xx < abs(shared.direction[1]):
    #     collision = "LEFT"
    # if shared.ball_xx > shared.columns - shared.direction[1] - 1:
    #     collision = "RIGHT"

    for line, column in get_line_between_points((shared.ball_yy, shared.ball_xx),
                                                (shared.ball_yy + shared.direction[0],
                                                 shared.ball_xx + shared.direction[1]),
                                                5):
        if (map_data[line, column] != 0):
            change_direction(line, column)
            return False
    #
    # if collision:
    #     print("Collision: {}!".format(collision))
    #     change_direction(collisions.get(collision))
    #     return False

    return True


def is_direction_changed():
    return map_data[shared.ball_yy + shared.direction[0]][shared.ball_xx + shared.direction[1]] != 0


def change_direction(collision):
    print()
    shared.direction = (
        shared.direction[0] * map_data[collision[0]][collision[1]][0],
        shared.direction[1] * map_data[collision[0]][collision[1]][1])
    print("New direction: {}".format(shared.direction))


def change_direction(line, column):
    print()
    shared.direction = (
        shared.direction[0] * map_data[line][column][0],
        shared.direction[1] * map_data[line][column][1])
    print("New direction: {}".format(shared.direction))
