from collections import OrderedDict

import game_map

my_dictionary = OrderedDict()

tests = [
    ["up_down_z", (10, 10), (12, 10), 1,
     [(10, 10), (11, 10), (12, 10)]],
    # ["left_right_z", (10, 10), (10, 12), 1,
    #  [(10, 10), (11, 10), (12, 10)]]
]


def test_framework():
    for test in tests:
        points = game_map.get_line_between_points(test[1], test[2], test[3])

        if points != test[4]:
            print("Test {} failed!".format(test[0]))
            quit()
            print("")
        print("Test {} passed".format(test[0]))


test_framework()
