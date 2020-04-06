import numpy as np

import shared

map_data = cells = np.zeros((shared.lines, shared.columns), dtype=tuple)


def create_map():
    """ Create the initial map. """
    for line in range(0, shared.lines - shared.handle_altitude):
        map_data[line][0] = (0, 2)
        map_data[line][shared.columns - 1] = (0, -2)

    for column in range(0, shared.columns):
        map_data[0, column] = (2, 0)
        if column <= shared.left_space or column > shared.columns - shared.left_space:
            map_data[shared.lines - shared.handle_altitude - 1, column] = (-2, 0)


def handles():
    pass


def is_direction_changed():
    print("Current position: ({},{}). Direction: ({},{}). Value: {}".format(shared.ball_yy,
                                                                            shared.ball_xx,
                                                                            shared.direction[0],
                                                                            shared.direction[1],
          map_data[shared.ball_yy + shared.direction[0]][shared.ball_xx + shared.direction[1]]))
    return map_data[shared.ball_yy + shared.direction[0]][shared.ball_xx + shared.direction[1]] != 0
