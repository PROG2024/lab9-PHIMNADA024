"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_add_area_with_two_positive_radius_circle(self):
        """Test that add_area with two circle having positive radius."""
        Circle.add_area(Circle(15), Circle(20))
        Circle.add_area(Circle(3), Circle(4))

    def test_add_area_has_one_circle_with_radius_zero(self):
        """Test that add_area that has 1 circle with radius 0 works the same regardless of which circle has radius 0."""
        Circle.add_area(Circle(0), Circle(3))
        Circle.add_area(Circle(3), Circle(0))

    def test_if_radius_is_negative(self):
        """Raises exception if the radius is negative"""
        with self.assertRaises(Exception):
            c1 = Circle(-2)
            c2 = Circle(-4)
