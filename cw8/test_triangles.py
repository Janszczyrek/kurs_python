import pytest
from triangles import Triangle
from points import Point


class TestTriangles:
    @pytest.fixture(scope="class")
    def triangle1(self):
        return Triangle(1, 1, 2, 3, 4, 1)

    @pytest.fixture(scope="class")
    def triangle1b(self):
        return Triangle(2, 3, 1, 1, 4, 1)

    @pytest.fixture(scope="class")
    def triangle1c(self):
        return Triangle(4, 1, 1, 1, 2, 3)

    @pytest.fixture(scope="class")
    def triangle2(self):
        return Triangle(6, 2, 1, 5, 1, 1)

    @pytest.fixture(scope="class")
    def triangle3(self):
        return Triangle(-1, 0, 1, 0, 0, 2)

    @pytest.fixture(scope="class")
    def triangle3(self):
        return Triangle(-1, -2, 3, 4, -5, -6)

    @pytest.fixture(scope="class")
    def triangle4(self):
        return Triangle(1, 1, 2, 3, 4, 1)

    @pytest.fixture(scope="class")
    def triangle5(self):
        return Triangle(-2, 3, 4, 2, 6, 1)

    @pytest.fixture(scope="class")
    def triangle5(self):
        return Triangle(-2, 3, 4, 2, 6, 1)

    @pytest.fixture(scope="class")
    def triangle6(self):
        return Triangle(1, 1, 4, 1, 2, 4)

    @pytest.fixture(scope="class")
    def triangle6_moved(self):
        return Triangle(6, 3, 5, 0, 8, 0)

    @pytest.fixture(scope="class")
    def triangle7(self):
        return Triangle(-1, 0, 1, 0, 0, 2)

    @pytest.fixture(scope="class")
    def triangle7_1(self):
        return Triangle(1, 0, 1 / 2, 1, 0, 0)

    @pytest.fixture(scope="class")
    def triangle7_2(self):
        return Triangle(-1, 0, -1 / 2, 1, 0, 0)

    @pytest.fixture(scope="class")
    def triangle7_3(self):
        return Triangle(1 / 2, 1, -1 / 2, 1, 0, 0)

    @pytest.fixture(scope="class")
    def triangle7_4(self):
        return Triangle(0, 2, -1 / 2, 1, 1 / 2, 1)

    def test_init(self):
        with pytest.raises(ValueError, match="Podane punkty są współliniowe"):
            t1 = Triangle(1, 1, 2, 2, 3, 3)
            t2 = Triangle(-1, -1, -1, 2, -1, 3)
            t3 = Triangle(-5, -4, 2, -2, 16, 2)

    def test_from_points(self, triangle1):
        with pytest.raises(ValueError, match="Trójkąt musi mieć trzy punkty!"):
            t1 = Triangle.from_points((Point(4, 1), Point(2, 3)))
            t2 = Triangle.from_points([Point(4, 1), Point(2, 3)])
        assert triangle1 == Triangle.from_points(
            (Point(4, 1), Point(2, 3), Point(1, 1))
        )
        assert triangle1 == Triangle.from_points(
            [Point(2, 3), Point(1, 1), Point(4, 1)]
        )
        assert triangle1 == Triangle.from_points(
            [Point(1, 1), Point(4, 1), Point(2, 3)]
        )

    def test_hash(self, triangle1, triangle1b, triangle1c):
        assert hash(triangle1) == hash(triangle1b)
        assert hash(triangle1) == hash(triangle1c)
        assert hash(triangle1b) == hash(triangle1c)

    def test_print(self, triangle1):
        assert str(triangle1) == "[(1, 1), (2, 3), (4, 1)]"
        assert repr(triangle1) == "Triangle(1, 1, 2, 3, 4, 1)"

    def test_equal(self, triangle1, triangle1b, triangle1c):
        assert triangle1 == triangle1b
        assert triangle1 == triangle1c
        assert triangle1b == triangle1c

    def test_center(self, triangle2, triangle3):
        assert triangle2.center == Point(8 / 3, 8 / 3)
        assert triangle3.center == Point(-1, (-4 / 3))

    def test_area(self, triangle4, triangle5):
        assert triangle4.area() == 3
        assert triangle5.area() == 2

    def test_move(self, triangle6, triangle6_moved):
        assert triangle6.move(4, -1) == triangle6_moved

    def test_make4(self, triangle7, triangle7_1, triangle7_2, triangle7_3, triangle7_4):
        assert set(triangle7.make4()) == {
            triangle7_1,
            triangle7_2,
            triangle7_3,
            triangle7_4,
        }

    def test_bounding_box(self, triangle1, triangle3):
        assert triangle1.top == 3
        assert triangle1.left == 1
        assert triangle1.bottom == 1
        assert triangle1.right == 4
        assert triangle1.width == 3
        assert triangle1.height == 2

        assert triangle3.top == 4
        assert triangle3.left == -5
        assert triangle3.bottom == -6
        assert triangle3.right == 3
        assert triangle3.width == 8
        assert triangle3.height == 10

        assert triangle1.topleft == Point(1, 3)
        assert triangle1.bottomleft == Point(1, 1)
        assert triangle1.topright == Point(4, 3)
        assert triangle1.bottomright == Point(4, 1)

        assert triangle3.topleft == Point(-5, 4)
        assert triangle3.bottomleft == Point(-5, -6)
        assert triangle3.topright == Point(3, 4)
        assert triangle3.bottomright == Point(3, -6)

    if __name__ == "__main__":
        pytest.main()
