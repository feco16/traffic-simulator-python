import math

import numpy as np

import shared

PI = 3.14159265
map_data = cells = np.zeros((shared.lines, shared.columns), dtype=tuple)

number = 3

collision = None
collisions = {"UP": (0, 1), "DOWN": (shared.lines - 1, 1), "LEFT": (1, 0),
              "RIGHT": (1, shared.columns - 1)}

default_positions = {"UP": (1, None), "DOWN": (shared.lines - 2, None), "LEFT": (None, 1),
                     "RIGHT": (None, shared.columns - 2)}

obstacles = (
    ### MAP ###
    ###HORIZONTAL###
    ((0, 0), (0, shared.columns - 1)),
    ((shared.lines - 1, 0), (shared.lines - 1, shared.columns - 1)),
    ###VERTICAL###
    ((0, 0), (shared.lines - 1, 0)),
    ((0, shared.columns - 1), (shared.lines - 1, shared.columns - 1)),

    # ((50, 50), (70, 50)),
    # ((50, 50), (270, 100)),
    # # ((70, 72), (100, 102)),
    # ((270, 100), (160, 150)),
    # ((160, 170), (50, 50)),

    ((300, 1), (349, 50)),
    ((300, 199), (349, 150)),
)


def create_map():
    """ Create the initial map. """
    pass
    # for line in range(0, shared.lines):
    #     map_data[line][0] = (1, -1)
    #     map_data[line][shared.columns - 1] = (1, -1)
    #
    # for column in range(0, shared.columns):
    #     map_data[0, column] = (-1, 1)
    #     # if column <= shared.left_space or column > shared.columns - shared.left_space:
    #     map_data[shared.lines - 1, column] = (-1, 1)


def create_obstacles():
    for obs in obstacles:
        for line, column in get_line_between_points(obs[0], obs[1]):
            map_data[line, column] = obs


def get_line_between_points(A, B, multiply=1):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    if x1 != x2:
        m = (y1 - y2) / (x1 - x2)
        b = (x1 * y2 - x2 * y1) / (x1 - x2)

        y = [(int(x), int(m * x + b)) for x in np.arange(x1, x2 + (1 if x2 > x1 else -1),
                                                         (1 if x2 > x1 else -1) / multiply)]
    else:
        y = [(x1, int(my)) for my in np.arange(y1, y2 + (1 if y2 > y1 else -1),
                                               (1 if y2 > y1 else -1) / multiply)]
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
    # for line, column in get_line_between_points((shared.ball_yy, shared.ball_xx),
    #                                             (shared.ball_yy + shared.direction[0],
    #                                              shared.ball_xx + shared.direction[1]),
    #                                             5):
    #     if (map_data[line, column] != 0):
    #         return change_direction(line, column)

    for obs in obstacles:
        if doIntersect(Point(obs[0][0], obs[0][1]),
                       Point(obs[1][0], obs[1][1]),
                       Point(shared.ball_yy, shared.ball_xx),
                       Point(shared.ball_yy + shared.direction[0],
                             shared.ball_xx + shared.direction[1])
                       ):
            collisionx, collisiony = get_collision_point(obs)
            return change_direction(obs, collisionx, collisiony)

    return True


def change_direction(obs, line, column):
    apply_change_immediately = False
    # if type(map_data[line][column][0]) != int:
    deflected_point, angle = get_deflected_point(obs, line, column)
    shared.direction = (
        # line - deflected_point[0] if angle > 0 else deflected_point[0] - line,
        #
        # column - deflected_point[1] if angle > 0 else deflected_point[1] - column
        deflected_point[0] - line,
        deflected_point[1] - column
    )
    shared.ball_yy = deflected_point[0]
    shared.ball_xx = deflected_point[1]
    apply_change_immediately = False
    # else:
    #     shared.direction = (
    #         shared.direction[0] * map_data[line][column][0],
    #         shared.direction[1] * map_data[line][column][1])
    print("Line, Column: ({}, {}). New direction: {}".format(line, column, shared.direction))
    return apply_change_immediately


def get_deflected_point(obs, line, column):
    # (Ax, Ay) = (map_data[line][column][0][0], map_data[line][column][0][1])
    # (Bx, By) = (map_data[line][column][1][0], map_data[line][column][1][1])
    (Ax, Ay) = (obs[0][0], obs[0][1])
    (Bx, By) = (obs[1][0], obs[1][1])
    (Cx, Cy) = (shared.ball_yy, shared.ball_xx)
    (Dx, Dy) = (shared.ball_yy + shared.direction[0], shared.ball_xx + shared.direction[1])

    m1 = (By - Ay) / (Bx - Ax if Bx != Ax else 0.000001);
    A = math.atan(m1) * 180 / PI;

    m2 = (Dy - Cy) / (Dx - Cx if Dx != Cx else 0.000001);
    B = math.atan(m2) * 180 / PI;

    angle = round(A - B)

    rad_angle = math.radians(angle)

    distance = 5
    deflected_point = (
        round(line + distance * math.sin(rad_angle)),
        round(column + distance * math.cos(rad_angle)))

    print("Angle: {}, Deflected point: {}".format(angle, deflected_point))
    return deflected_point, angle


def get_collision_point(obs):
    (Ax, Ay) = (obs[0][0], obs[0][1])
    (Bx, By) = (obs[1][0], obs[1][1])
    (Cx, Cy) = (shared.ball_yy, shared.ball_xx)
    (Dx, Dy) = (shared.ball_yy + shared.direction[0], shared.ball_xx + shared.direction[1])

    r = ((Ay - Cy) * (Dx - Cx) - (Ax - Cx) * (Dy - Cy)) / (
            (Bx - Ax) * (Dy - Cy) - (By - Ay) * (Dx - Cx))
    s = ((Ay - Cy) * (Bx - Ax) - (Ax - Cx) * (By - Ay)) / (
            (Bx - Ax) * (Dy - Cy) - (By - Ay) * (Dx - Cx))

    collisionx, collisiony = Ax + r * (Bx - Ax), Ay + s * (By - Ay)
    print("Collision point: ({}, {}). Obstacle: {}".format(collisionx, collisiony, obs))
    return round(collisionx), round(collisiony)


# A Python3 program to find if 2 given line segments intersect or not

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Given three colinear points p, q, r, the function checks if


# point q lies on line segment 'pr'
def onSegment(p, q, r):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Colinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):

        # Clockwise orientation
        return 1
    elif (val < 0):

        # Counterclockwise orientation
        return 2
    else:

        # Colinear orientation
        return 0


# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def doIntersect(p1, q1, p2, q2):
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True

    # If none of the cases
    return False
