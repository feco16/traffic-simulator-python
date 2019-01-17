import shared
from simulate import one_clock

repeats = 10000
clock_timer = 10000


def calculate(case):
    sum = 0
    counter = repeats
    while counter:
        while shared.clock_counter < clock_timer:
            one_clock()
        sum += shared.total_speed()
        counter -= 1

    score = round(sum/repeats, 3)
    # print_total_speed(case, score)
    return score


def print_total_speed(case, total_speed):
    print(case + " total speed:{}".format(total_speed))
    print("        cars finished:{}".format(shared.finished_cars))


def one_line():
    shared.init_configuration()
    shared.lines = 1
    calculate("One line")


def multiple_line_rule(line):
    shared.lines = line
    shared.init_configuration()
    shared.use_rule = True
    calculate("{} line with rule".format(line))


def multiple_line_no_rule(line):
    shared.init_configuration()
    shared.lines = line
    shared.use_rule = False
    calculate("{} line without rule".format(line))


def car_number_with_rule(car_list, line):
    scores = [0] * len(car_list)
    index = 0
    for cars in car_list:
        shared.init_configuration()
        shared.lines = line
        shared.use_rule = True
        shared.car_number = cars
        scores[index] = calculate("{} line with rule".format(line))
        index += 1
    print(scores)
    print(sum(scores))
    return scores


def car_number_no_rule(car_list, line):
    scores = [0] * len(car_list)
    for cars in car_list:
        shared.init_configuration()
        shared.lines = line
        shared.use_rule = False
        shared.car_number = cars
        scores[cars] = calculate("{} line no rule".format(line))
    print(scores)
    print(sum(scores))

# def test():
    # one_line()
    # multiple_line_rule(2)
    # multiple_line_no_rule(2)
    # multiple_line_rule(3)
    # multiple_line_no_rule(3)
    # multiple_line_rule(4)
    # multiple_line_no_rule(4)
    # multiple_line_rule(5)
    # multiple_line_no_rule(5)
    # car_number_with_rule(5)
    # car_number_no_rule(5)

# test()

