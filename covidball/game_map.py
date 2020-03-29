import numpy as np

import shared



margin = 0

map_data = cells = np.zeros((shared.lines + margin, shared. columns + margin), dtype=tuple)


def create_map():
    for line in range(0, shared.lines - shared.handle_altitude):
        map_data[line][0] = (0, 2)
        map_data[line][shared.columns - 1] = (0, -2)

    for column in range(0, shared.columns):
        map_data[0, column] = (2, 0)
        if column <= shared.left_space or column > shared.columns - shared.left_space:
            map_data[shared.lines - shared.handle_altitude - 1, column] = (-2, 0)

def handles():
    pass