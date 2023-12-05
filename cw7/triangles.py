from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        segment1Length = Point(x1, y1).segment_length(Point(x2, y2))
        segment2Length = Point(x1, y1).segment_length(Point(x3, y3))
        segment3Length = Point(x2, y2).segment_length(Point(x3, y3))
        if (
            (segment1Length + segment2Length <= segment3Length)
            or (segment1Length + segment3Length <= segment2Length)
            or (segment2Length + segment3Length <= segment1Length)
        ):
            raise ValueError("Podane punkty są współliniowe")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return (
            f"[({self.pt1.x}, {self.pt1.y}), "
            f"({self.pt2.x}, {self.pt2.y}), "
            f"({self.pt3.x}, {self.pt3.y})]"
        )

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return (
            f"Triangle({self.pt1.x}, {self.pt1.y}, "
            f"{self.pt2.x}, {self.pt2.y}, "
            f"{self.pt3.x}, {self.pt3.y})"
        )

    def __eq__(self, other):  # obsługa tr1 == tr2
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        return set((self.pt1, self.pt2, self.pt3)) == set(
            (other.pt1, other.pt2, other.pt3)
        )

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    def __hash__(self):
        sortedVertices = sorted(
            (self.pt1, self.pt2, self.pt3), key=lambda p: [p.x, p.y]
        )
        return hash(
            (sortedVertices[0], sortedVertices[1], sortedVertices[2])
        )  # bazujemy na tuple, immutable points

    def center(self):  # zwraca środek (masy) trójkąta
        return Point(
            (self.pt1.x + self.pt2.x + self.pt3.x) / 3,
            (self.pt1.y + self.pt2.y + self.pt3.y) / 3,
        )

    def area(self):  # pole powierzchni
        return (
            abs(
                self.pt1.x * self.pt2.y
                + self.pt2.x * self.pt3.y
                + self.pt3.x * self.pt1.y
                - self.pt2.x * self.pt1.y
                - self.pt3.x * self.pt2.y
                - self.pt1.x * self.pt3.y
            )
            / 2
        )

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)
        self.pt3 = self.pt3 + Point(x, y)
        return self

    # zwraca krotkę czterech mniejszych
    #     A       po podziale    A
    #    / \                    / \
    #   /   \                  +---+
    #  /     \                / \ / \
    # C-------B              C---+---B
    def make4(self):
        point1 = self.pt1.segment_center(self.pt2)
        point2 = self.pt1.segment_center(self.pt3)
        point3 = self.pt2.segment_center(self.pt3)
        return (
            Triangle(self.pt1.x, self.pt1.y, point1.x, point1.y, point2.x, point2.y),
            Triangle(self.pt2.x, self.pt2.y, point1.x, point1.y, point3.x, point3.y),
            Triangle(self.pt3.x, self.pt3.y, point2.x, point2.y, point3.x, point3.y),
            Triangle(point1.x, point1.y, point2.x, point2.y, point3.x, point3.y),
        )


# Kod testujący moduł.

import unittest


class TestTriangle(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError, Triangle, 1, 1, 2, 2, 3, 3)
        self.assertRaises(ValueError, Triangle, -1, -1, -1, 2, -1, 3)
        self.assertRaises(ValueError, Triangle, -5, -4, 2, -2, 16, 2)

    def test_hash(self):
        self.assertEqual(
            hash(Triangle(1, 1, 2, 3, 4, 1)), hash(Triangle(1, 1, 4, 1, 2, 3))
        )
        self.assertEqual(
            hash(Triangle(1, -234, 123, 3, 4, 342)),
            hash(Triangle(4, 342, 1, -234, 123, 3)),
        )
        self.assertEqual(
            hash(Triangle(1, 1, 2, 3, 4, 1)), hash(Triangle(1, 1, 4, 1, 2, 3))
        )

    def test_print(self):
        self.assertEqual(str(Triangle(1, 2, 2, 2, 3, 3)), "[(1, 2), (2, 2), (3, 3)]")
        self.assertEqual(repr(Triangle(1, 2, 2, 2, 3, 3)), "Triangle(1, 2, 2, 2, 3, 3)")

    def test_equal(self):
        self.assertEqual(Triangle(1, 1, 2, 3, 4, 1), Triangle(1, 1, 2, 3, 4, 1))
        self.assertEqual(Triangle(1, 1, 2, 3, 4, 1), Triangle(1, 1, 4, 1, 2, 3))
        self.assertEqual(Triangle(1, 1, 2, 3, 4, 1), Triangle(2, 3, 1, 1, 4, 1))
        self.assertEqual(Triangle(1, 1, 2, 3, 4, 1), Triangle(2, 3, 4, 1, 1, 1))
        self.assertEqual(Triangle(1, 1, 2, 3, 4, 1), Triangle(4, 1, 2, 3, 1, 1))
        self.assertEqual(Triangle(1, 1, 2, 3, 4, 1), Triangle(4, 1, 1, 1, 2, 3))

    def test_center(self):
        self.assertEqual(Triangle(6, 2, 1, 5, 1, 1).center(), Point(8 / 3, 8 / 3))
        self.assertEqual(Triangle(-1, -2, 3, 4, -5, -6).center(), Point(-1, (-4 / 3)))

    def test_area(self):
        self.assertEqual(Triangle(1, 1, 2, 3, 4, 1).area(), 3)
        self.assertEqual(Triangle(-2, 3, 4, 2, 6, 1).area(), 2)

    def test_move(self):
        self.assertEqual(
            Triangle(1, 1, 4, 1, 2, 4).move(4, -1), Triangle(6, 3, 5, 0, 8, 0)
        )
        self.assertEqual(
            Triangle(-1, 3, 4, 2, -10, 3).move(-10, -1), Triangle(-11, 2, -6, 1, -20, 2)
        )

    def test_make4(self):
        self.assertEqual(
            set(Triangle(-1, 0, 1, 0, 0, 2).make4()),
            {
                Triangle(-1, 0, -1 / 2, 1, 0, 0),
                Triangle(1, 0, 1 / 2, 1, 0, 0),
                Triangle(0, 2, -1 / 2, 1, 1 / 2, 1),
                Triangle(1 / 2, 1, -1 / 2, 1, 0, 0),
            },
        )
        self.assertEqual(
            set(Triangle(-1, 0, 1, 0, 0, 2).make4()),
            {
                Triangle(1, 0, 1 / 2, 1, 0, 0),
                Triangle(-1, 0, -1 / 2, 1, 0, 0),
                Triangle(1 / 2, 1, -1 / 2, 1, 0, 0),
                Triangle(0, 2, -1 / 2, 1, 1 / 2, 1),
            },
        )


if __name__ == "__main__":
    unittest.main()
