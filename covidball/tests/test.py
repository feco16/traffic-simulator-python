# (Ax, Ay) = (5, 1)
# (Bx, By) = (1, 3)
# (Cx, Cy) = (1, 2)
# (Dx, Dy) = (5, 2)

(Ax, Ay) = (1, 5)
(Bx, By) = (5, 1)
(Cx, Cy) = (1, 3)
(Dx, Dy) = (5, 3)


def get_deflected_point(line, column):
    (Ax, Ay) = (1, 5)
    (Bx, By) = (5, 1)
    (Cx, Cy) = (1, 3)
    (Dx, Dy) = (5, 3)

    m1 = (By - Ay) / (Bx - Ax);
    A = math.atan(m1) * 180 / PI;

    m2 = (Dy - Cy) / (Dx - Cx);
    B = math.atan(m2) * 180 / PI;

    angle = round(A - B)

    angle = math.radians(angle)

    distance = 5
    deflected_point = (column + distance * math.sin(angle), line + distance * math.cos(angle))
    return deflected_point
# 0
#
#  .
# . . . . .
#  .
# 5 .
#

def get_collision_point():
    r = ((Ay - Cy) * (Dx - Cx) - (Ax - Cx) * (Dy - Cy)) / (
                (Bx - Ax) * (Dy - Cy) - (By - Ay) * (Dx - Cx))
    s = ((Ay - Cy) * (Bx - Ax) - (Ax - Cx) * (By - Ay)) / (
                (Bx - Ax) * (Dy - Cy) - (By - Ay) * (Dx - Cx))


    print(r, s)

    (collisionx ,collisiony) = Ax+r *(Bx-Ax), Ay+s *(By-Ay)
    print(collisionx, collisiony)
    return collisiony, collisiony

collisionx ,collisiony = get_collision_point()

import math
import numpy
PI = 3.14159265

m1 = (By - Ay) / (Bx - Ax);
A = math.atan(m1) * 180 / PI;

m2 = (Dy - Cy) / (Dx - Cx);
B = math.atan(m2) * 180 / PI;



angle = round(A - B)
print(angle)

# angle = 45
#
# (collisionx, collisiony) = (0, 0)

angle = math.radians(angle)

for distance in numpy.arange(0, 10, math.sqrt(2)):
    print(collisionx + distance * math.sin(angle), collisiony + distance * math.cos(angle))