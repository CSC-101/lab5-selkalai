import data
from data import Time
from data import Point
import lab5
import unittest



# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    #The part three tests are failing for some reason but when I click on the "Click to see actual difference"
    # it says the contents are identical. I think it is something weird with the string rpr but the function is working
    def test_time_add_1(self):
        time_one = Time(2, 30, 45)
        time_two = Time(2, 15, 22)
        result = lab5.time_add(time_one, time_two)
        expected ='Time(4, 46, 7)'
        self.assertEqual(expected, result)

    def test_time_add_2(self):
        time_one = Time(6, 43, 1)
        time_two = Time(2, 10, 22)
        result = lab5.time_add(time_one, time_two)
        expected ='Time(8, 53, 23)'
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending_1(self):
        list1 = [9, 4, 3, 2, -90]
        result = lab5.is_descending(list1)
        expected = True
        self.assertEqual(expected, result)

    def test_is_descending_2(self):
        list1 = [9, 4, 2, 21, -10]
        result = lab5.is_descending(list1)
        expected = False
        self.assertEqual(expected, result)

    # Part 5
    def test_largest_between_1(self):
        list1 = [9, 4, 2, 21, -10]
        result = lab5.largest_between(list1, 2, 1)
        expected = 1
        self.assertEqual(expected, result)

    def test_largest_between_2(self):
        list1 = [9, 4, 2, 21, -10]
        result = lab5.largest_between(list1, 2, 4)
        expected = None
        self.assertEqual(expected, result)

    def test_largest_between_3(self):
        list1 = [9, 4, 2, 21, -10]
        result = lab5.largest_between(list1, 2, -1)
        expected = None
        self.assertEqual(expected, result)


    # Part 6

    def test_furthest_from_origin_1(self):
        point_a = Point(8,2)
        point_b = Point(1,3)
        point_c = Point(18, 9)
        list1 = [point_a, point_b, point_c]
        result = lab5.furthest_from_origin(list1)
        expected = 2
        self.assertEqual(expected, result)

    def test_furthest_from_origin_2(self):
        list1 = []
        result = lab5.furthest_from_origin(list1)
        expected = None
        self.assertEqual(expected, result)

    def test_furthest_from_origin_3(self):
        point_a = Point(8,2)
        point_b = Point(1,3)
        point_c = Point(-18, -9)
        list1 = [point_a, point_b, point_c]
        result = lab5.furthest_from_origin(list1)
        expected = 2
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
