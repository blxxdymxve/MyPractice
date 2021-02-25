from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Hexagon:
    def __init__(self, *points):
        self.points = list(points)

        self.sides = list()

        self.get_perimeter()

    def get_perimeter(self):
        self.perimeter = 0

        for i in range(len(self.points)):
            start = self.points[i - 1]
            end = self.points[i]

            side = sqrt((end.x - start.x)**2 + (end.y - start.y)**2)

            self.sides.append(side)

            self.perimeter += side

with open('coordinates.txt', 'r', encoding='utf8') as f:
    string = f.readline()
    x = str(string)[0]
    y = str(string)[2]
    a = Point(int(x), int(y))
    ABC = Hexagon(a)

print(ABC.perimeter)

# a = Point(0, 0)
#
# b = Point(0, 1)
#
# c = Point(2, 1)
#
# d = Point(2, 0)
#
# ABC = Hexagon(a, b, c, d)
#
# print(ABC.perimeter)