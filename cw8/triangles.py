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

    @property
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

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Trójkąt musi mieć trzy punkty!")
        return Triangle(
            points[0].x,
            points[0].y,
            points[1].x,
            points[1].y,
            points[2].x,
            points[2].y,
        )

    @property
    def top(self):
        return max([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y

    @property
    def left(self):
        return min([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x

    @property
    def bottom(self):
        return min([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y

    @property
    def right(self):
        return max([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x

    @property
    def width(self):
        return (
            max([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x
            - min([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x
        )

    @property
    def height(self):
        return (
            max([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y
            - min([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y
        )

    @property
    def topleft(self):
        return Point(
            min([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x,
            max([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y,
        )

    @property
    def bottomleft(self):
        return Point(
            min([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x,
            min([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y,
        )

    @property
    def topright(self):
        return Point(
            max([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x,
            max([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y,
        )

    @property
    def bottomright(self):
        return Point(
            max([self.pt1, self.pt2, self.pt3], key=lambda point: point.x).x,
            min([self.pt1, self.pt2, self.pt3], key=lambda point: point.y).y,
        )
