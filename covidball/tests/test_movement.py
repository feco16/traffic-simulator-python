""" Test movement methods"""
import inspect

import game_map
import shared

position_changing = 5

tests = [
    # ["minus_minus_up", (4, 54), (-5, -1), (1, 53)],
    # ["minus_plus_right", (10, shared.columns - 5), (-1, 5), (9, shared.columns -2)],
    # ["plus_plus_down", (shared.lines - 3, 120), (3, 5), (shared.lines - 2, 125)],
    # ["minus_z_obs", (100, 50), (-5, 0), (100, 50), (
    #     ((100, 10), (100, 150)),
    # ["minus_minus_obs", (100, 50), (-5, -5), (95, 55), (
    #     ((10, 45), (100, 45)),
    # )],
    ["plus_plus_obs", (106, 61), (3, 3), (95, 55), (
        ((50, 50), (270, 100)),
    )]
]


def plus_plus_down():
    print("TESt {}".format(inspect.currentframe().f_code.co_name))
    game_map.create_map()
    shared.ball_yy = 347
    shared.ball_xx = 10
    shared.direction = (3, 5)
    game_map.move_ball()

    print("Ball position after: ({}, {})".format(shared.ball_yy, shared.ball_xx))
    if shared.ball_yy != 348 or shared.ball_xx != 15:
        print("Test {} failed!".format(inspect.currentframe().f_code.co_name))
        quit()


def plus_plus_right():
    print("TEST plus plus right")
    game_map.create_map()
    shared.ball_yy = 10
    shared.ball_xx = shared.columns - 5
    shared.direction = (1, position_changing)

    game_map.move_ball()

    print("Ball position after: ({}, {})".format(shared.ball_yy, shared.ball_xx))
    if shared.ball_yy != 11 or shared.ball_xx != 198:
        print("Test {} failed!".format(inspect.currentframe().f_code.co_name))
        quit()
    print("")


def move_ball_vertical():
    position_changing = 5
    game_map.create_map()
    shared.ball_yy = shared.lines - position_changing
    shared.ball_xx = int(shared.columns / 2)
    shared.direction = (position_changing - 1, 0)
    print("Ball position before: ({}, {})".format(shared.ball_yy, shared.ball_xx))

    game_map.move_ball()

    print("Ball position after: ({}, {})".format(shared.ball_yy, shared.ball_xx))
    if shared.ball_yy != shared.lines - position_changing + shared.direction[0]:
        print("Test {} failed!".format(inspect.currentframe().f_code.co_name))
        quit()


def move_ball_horizontal():
    print("Move ball horizontal")
    game_map.create_map()
    shared.ball_yy = 10
    shared.ball_xx = shared.columns - position_changing
    shared.direction = (0, position_changing)
    game_map.move_ball()

    print("Ball position after: ({}, {})".format(shared.ball_yy, shared.ball_xx))
    if shared.ball_yy != 10 or shared.ball_xx != 198:
        print("Test {} failed!".format(inspect.currentframe().f_code.co_name))
        quit()


def plus_minus_from_rigth():
    print("TESt {}".format(inspect.currentframe().f_code.co_name))
    game_map.create_map()
    shared.ball_yy = 10
    shared.ball_xx = shared.columns - 2
    shared.direction = (1, -5)
    game_map.move_ball()

    print("Ball position after: ({}, {})".format(shared.ball_yy, shared.ball_xx))
    if shared.ball_yy != 11 or shared.ball_xx != 193:
        print("Test {} failed!".format(inspect.currentframe().f_code.co_name))
        quit()


def test_framework():
    for test in tests:
        game_map.create_map()
        shared.ball_yy = test[1][0]
        shared.ball_xx = test[1][1]
        shared.direction = (test[2][0], test[2][1])

        if len(test) == 5:
            game_map.obstacles = test[4]
            game_map.create_obstacles()
            # game_map.move_ball()


        game_map.move_ball()

        if shared.ball_yy != test[3][0] or shared.ball_xx != test[3][1]:
            print("Position: ({}, {}) not as expected: ({}, {})".
                  format(shared.ball_yy, shared.ball_xx, test[3][0], test[3][1]))
            print("Test {} failed!".format(test[0]))
            print("")
        else:
            print("Test {} passed".format(test[0]))


test_framework()
