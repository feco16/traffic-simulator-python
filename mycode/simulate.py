import random as rand

import shared


def add_car():

    for line in range(0, shared.lines):
        chance = rand.randint(0, shared.count_zero(line))
        if chance > shared.car_number - shared.count_nonzero(line):
            continue
        speed = rand.randint(1, shared.gears)
        if shared.cells[line][0] == 0:
            shared.cells[line][0] = (shared.timer, speed, False)


def clock(line, rule):
    for cell_index in range(shared.columns - 1, -1, -1):
        cell = shared.cells[line][cell_index]
        if type(cell) == tuple:
            cell = (cell[0] - cell[1], cell[1], False)
            if cell[0] <= 0:
                if cell_index == shared.columns - 1:
                    shared.cells[line][cell_index] = 0
                    shared.finished_cars += 1
                else:
                    if shared.cells[line][cell_index + 1] == 0:
                        # there is space ahead - move forward
                        shared.cells[line][cell_index + 1] = (shared.timer, shared.cells[line][cell_index][1], False)
                        shared.cells[line][cell_index] = 0
                        shared.forward_steps += 1
                    else:
                        if shared.lines  == 1:
                            shared.blocked_cars += 1
                        else:
                            if rule:
                                change_line_with_rule(line, cell_index)
                            else:
                                change_line_without_rule(line, cell_index)
            else:
                shared.cells[line][cell_index] = cell


def change_line_with_rule(line, column):
    if line < shared.lines - 1:
        if shared.cells[line+1][column] == 0:
            if column == 0 or shared.cells[line+1][column-1] == 0:
                shared.cells[line+1][column] = (shared.cells[line][column][0], shared.cells[line][column][1], True)
                shared.cells[line][column] = 0
                shared.line_changes += 1
                return
    shared.cells[line][column] = (shared.cells[line][column][0], shared.cells[line][column][1], False)
    shared.blocked_cars += 1


def change_line_without_rule(line, column):
    if line < shared.lines - 1:
        if shared.cells[line+1][column] == 0 and (shared.cells[line+1][column-1] == 0 or column == 0):
            shared.cells[line+1][column] = (shared.cells[line][column][0], shared.cells[line][column][1], True)
            shared.cells[line][column] = 0
            shared.line_changes += 1
            return
        if line > 0 and shared.cells[line-1][column] == 0 and (shared.cells[line-1][column-1] == 0 or column == 0):
            shared.cells[line-1][column] = (shared.cells[line][column][0], shared.cells[line][column][1], True)
            shared.cells[line][column] = 0
            shared.line_changes += 1
            return
    shared.blocked_cars += 1


def align_to_right():
    for line in range(shared.lines - 1, 0, -1):
        for cell_index in range(shared.columns - 1, -1, -1):
            cell = shared.cells[line][cell_index]
            if type(cell) == tuple and not cell[2]:
                if shared.cells[line - 1][cell_index] == 0 and shared.cells[line - 1][cell_index - 1] == 0:
                    shared.cells[line - 1][cell_index] = (shared.cells[line][cell_index][0], shared.cells[line][cell_index][1], False)
                    shared.cells[line][cell_index] = 0
                    shared.right_aligns += 1


def one_clock():
    for line in range(0, shared.lines):
        clock(line, shared.use_rule)
    if shared.lines > 1 and shared.use_rule:
        align_to_right()
    add_car()
    shared.clock_counter += 1

