import math
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):  # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

    def segment_length(self, other):  # długość odcinka między dwoma punktami
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def segment_center(self, other):  # środek odcinka
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def test_print(self):
        self.assertEqual(str(Point(1, -1)), "(1, -1)")
        self.assertEqual(repr(Point(1, -1)), "Point(1, -1)")

    def test_equal(self):
        self.assertEqual(Point(2, 2) == Point(2, 2), True)
        self.assertEqual(Point(2, 2) == Point(1, 2), False)
        self.assertEqual(Point(2, 2) != Point(1, 2), True)
        self.assertEqual(Point(2, 2) != Point(2, 2), False)

    def test_add(self):
        self.assertEqual(Point(0, 0) + Point(0, 0), Point(0, 0))
        self.assertEqual(Point(10, 0) + Point(0, 5), Point(10, 5))
        self.assertEqual(Point(5, 1) + Point(-2, 5), Point(3, 6))

    def test_substract(self):
        self.assertEqual(Point(0, 0) - Point(0, 0), Point(0, 0))
        self.assertEqual(Point(0, 0) - Point(-1, -1), Point(1, 1))
        self.assertEqual(Point(7, 7) - Point(4, 2), Point(3, 5))

    def test_multiply(self):
        self.assertEqual(Point(0, 0) * Point(-1, -1), 0)
        self.assertEqual(Point(1, 1) * Point(5, 4), 9)
        self.assertEqual(Point(-5, 4) * Point(4, -5), -40)

    def test_cross(self):
        self.assertEqual(Point(3, 4).cross(Point(-4, 3)), 25)
        self.assertEqual(Point(0, 4).cross(Point(0, 3)), 0)
        self.assertEqual(Point(2, 5).cross(Point(-1, -2)), 1)

    def test_length(self):
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertEqual(Point(0, 1).length(), 1)
        self.assertEqual(Point(1, 0).length(), 1)
        self.assertEqual(Point(1, 1).length(), math.sqrt(2))
        self.assertEqual(Point(3, 4).length(), 5)

    def test_segment_length(self):
        self.assertEqual(Point(0, 0).segment_length(Point(1, 1)), math.sqrt(2))
        self.assertEqual(Point(-2, -2).segment_length(Point(-8, -10)), 10)
        self.assertEqual(Point(-3, 1).segment_length(Point(1, -2)), 5)
    def test_segment_center(self):
        self.assertEqual(Point(0,0).segment_center(Point(0,-6)),Point(0,-3))
        self.assertEqual(Point(0,0).segment_center(Point(5,5)),Point(2.5,2.5))
        self.assertEqual(Point(4,-4).segment_center(Point(-8,2)),Point(-2,-1))
        self.assertEqual(Point(-8,2).segment_center(Point(4,-4)),Point(-2,-1))


if __name__ == "__main__":
    unittest.main()
