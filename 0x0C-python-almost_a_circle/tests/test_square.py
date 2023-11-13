from io import StringIO
import unittest
from unittest.mock import patch

from models.rectangle import Rectangle
from models.square import Square

"""Defines Unittests for Square class"""


class TestSquare(unittest.TestCase):
    """Unittests for the new instance of the Square Class"""

    def test_square_is_base(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_square_with_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_square_with_one_arguments(self):
        s1 = Square(1)
        s2 = Square(2)
        obj2 = [s2.id, s2.size, s2.x, s2.y]
        expected_result = [s1.id + 1, 2, 0, 0]
        self.assertEqual(obj2, expected_result)

    def test_square_with_two_arguments(self):
        s1 = Square(10, 2)
        s2 = Square(20, 2)
        obj2 = [s2.id, s2.size, s2.x, s2.y]
        expected_result = [s1.id + 1, 20, 2, 0]
        self.assertEqual(obj2, expected_result)

    def test_square_with_three_arguments(self):
        s1 = Square(10, 2, 3)
        s2 = Square(20, 2, 4)
        obj2 = [s2.id, s2.size, s2.x, s2.y]
        expected_result = [s1.id + 1, 20, 2, 4]
        self.assertEqual(obj2, expected_result)

    def test_square_with_four_arguments(self):
        s = Square(10, 2, 3, 3)
        obj2 = [s.id, s.height, s.x, s.y]
        expected_result = [3, 10, 2, 3]
        self.assertEqual(obj2, expected_result)

    def test_square_with_more_than_four_arguments(self):
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1, 1)


class TestSquareSize(unittest.TestCase):
    """Unittest for the size attribute of the Square class"""

    def test_size_setter_getter(self):
        s = Square(1)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_size_with_large_number(self):
        s = Square(99999999999999999)
        self.assertEqual(s.size, 99999999999999999)

    def test_size_type_error_str(self):
        with self.assertRaises(TypeError):
            Square('yousef', 0, 0, 9)

    def test_size_type_error_float(self):
        with self.assertRaises(TypeError):
            Square(3.5, 0, 0, 9)

    def test_size_type_error_list(self):
        with self.assertRaises(TypeError):
            Square([1, 2, 3], 0, 0, 9)

    def test_size_type_error_tuple(self):
        with self.assertRaises(TypeError):
            Square((1,), 0, 0, 9)

    def test_size_type_error_set(self):
        with self.assertRaises(TypeError):
            Square({1, 2}, 0, 0, 9)

    def test_size_type_error_dict(self):
        with self.assertRaises(TypeError):
            Square({'a': 1, 'b': 2}, 0, 0, 9)

    def test_size_type_error_bool(self):
        with self.assertRaises(TypeError):
            Square(True, 10, 0, 0, 9)

    def test_size_with_complex_number(self):
        with self.assertRaises(TypeError):
            Square(complex(5, 7), 0, 0, 9)

    def test_size_with_INF(self):
        with self.assertRaises(TypeError):
            Square(float('inf'), 0, 0, 9)

    def test_size_with_negative_INF(self):
        with self.assertRaises(TypeError):
            Square(float('-inf'), 0, 0, 9)

    def test_size_with_negative(self):
        with self.assertRaises(ValueError):
            Square(-10, 0, 0, 9)

    def test_size_with_zero(self):
        with self.assertRaises(ValueError):
            Square(0, 0, 0, 9)


class TestSquareX(unittest.TestCase):
    """Unittest for the x attribute of the Square class"""

    def test_x_setter_getter(self):
        s = Square(1)
        s.x = 10
        self.assertEqual(s.x, 10)

    def test_x_with_zero(self):
        s = Square(10, 0, 0, 9)
        self.assertEqual(s.x, 0)

    def test_x_with_large_number(self):
        r = Square(5, 99999999999999999)
        self.assertEqual(r.x, 99999999999999999)

    def test_x_type_error_str(self):
        with self.assertRaises(TypeError):
            Square(10, 'yousef', 0, 9)

    def test_x_type_error_float(self):
        with self.assertRaises(TypeError):
            Square(10, 3.5, 0, 9)

    def test_x_type_error_list(self):
        with self.assertRaises(TypeError):
            Square(10, [1, 2, 3], 0, 9)

    def test_x_type_error_tuple(self):
        with self.assertRaises(TypeError):
            Square(10, (1,), 0, 9)

    def test_x_type_error_set(self):
        with self.assertRaises(TypeError):
            Square(10, {1, 2}, 0, 9)

    def test_x_type_error_dict(self):
        with self.assertRaises(TypeError):
            Square(10, {'a': 1, 'b': 2}, 0, 9)

    def test_size_type_error_bool(self):
        with self.assertRaises(TypeError):
            Square(10, True, 0, 9)

    def test_x_with_complex_number(self):
        with self.assertRaises(TypeError):
            Square(10, complex(5, 7), 0, 9)

    def test_x_with_INF(self):
        with self.assertRaises(TypeError):
            Square(10, float('inf'), 0, 9)

    def test_x_with_negative_INF(self):
        with self.assertRaises(TypeError):
            Square(10, float('-inf'), 0, 9)

    def test_x_with_negative(self):
        with self.assertRaises(ValueError):
            Square(10, -10, 0, 9)


class TestSquareY(unittest.TestCase):
    """Unittest for the y attribute of the Square class"""

    def test_y_setter_getter(self):
        s = Square(1)
        s.y = 10
        self.assertEqual(s.y, 10)

    def test_y_with_zero(self):
        s = Square(10, 1, 0, 9)
        self.assertEqual(s.y, 0)

    def test_y_with_large_number(self):
        s = Square(5, 0, 99999999999999999)
        self.assertEqual(s.y, 99999999999999999)

    def test_y_type_error_str(self):
        with self.assertRaises(TypeError):
            Square(10, 10, 'yousef', 9)

    def test_y_type_error_float(self):
        with self.assertRaises(TypeError):
            Square(10, 10, 3.5, 9)

    def test_y_type_error_list(self):
        with self.assertRaises(TypeError):
            Square(10, 12, [1, 2, 3], 9)

    def test_y_type_error_tuple(self):
        with self.assertRaises(TypeError):
            Square(10, 12, (1,), 9)

    def test_y_type_error_set(self):
        with self.assertRaises(TypeError):
            Square(10, 12, {1, 2}, 9)

    def test_y_type_error_dict(self):
        with self.assertRaises(TypeError):
            Square(10, 12, {'a': 1, 'b': 2}, 9)

    def test_size_type_error_bool(self):
        with self.assertRaises(TypeError):
            Square(10, 12, True, 9)

    def test_y_with_complex_number(self):
        with self.assertRaises(TypeError):
            Square(10, 12, complex(5, 7), 9)

    def test_y_with_INF(self):
        with self.assertRaises(TypeError):
            Square(10, 12, float('inf'), 9)

    def test_y_with_negative_INF(self):
        with self.assertRaises(TypeError):
            Square(10, 12, float('-inf'), 9)

    def test_y_with_negative(self):
        with self.assertRaises(ValueError):
            Square(10, 12, -10, 9)


class TestSquareArea(unittest.TestCase):
    """Unittests for area method of the Square class"""

    def test_area_with_argument(self):
        with self.assertRaises(TypeError):
            s = Square(4)
            s.area('str')

    def test_area_with_small_numbers(self):
        s = Square(4, 0, 0, 10)
        self.assertEqual(s.area(), 16)

    def test_area_with_large_numbers(self):
        s = Square(99999999999999999, 0, 0, 10)
        self.assertEqual(s.area(), 9999999999999999800000000000000001)


class TestSquareDisplay(unittest.TestCase):
    """Unittests for display method of the Square class"""

    def test_display_with_arguments(self):
        with self.assertRaises(TypeError):
            s = Square(4)
            s.display('str')

    def test_display_with_zer0_x_zero_y(self):
        s = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_zero_y(self):
        s = Square(4, 2, 0, 9)
        expected_output = "  ####\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_zero_x(self):
        s = Square(4, 0, 2, 9)
        expected_output = "\n\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x_y(self):
        s = Square(4, 1, 2, 9)
        expected_output = "\n\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)


class TestSquareToDictionary(unittest.TestCase):
    """Unittest for to_dictionary method of the Square class"""

    def test_to_dictionary_with_arguments(self):
        with self.assertRaises(TypeError):
            s = Square(4)
            s.to_dictionary('str')

    def test_to_dictionary_Square_with_2_arguments(self):
        s1 = Square(10, 15)
        s2 = Square(4, 5)
        expected_output = {
            'id': s1.id + 1,
            'size': 4,
            'x': 5,
            'y': 0
        }
        self.assertEqual(s2.to_dictionary(), expected_output)

    def test_to_dictionary_Square_with_3_arguments(self):
        s1 = Square(10, 15)
        s2 = Square(4, 5, 2)
        expected_output = {
            'id': s1.id + 1,
            'size': 4,
            'x': 5,
            'y': 2
        }
        self.assertEqual(s2.to_dictionary(), expected_output)

    def test_to_dictionary_Square_with_4_arguments(self):
        s = Square(4, 5, 2, 1)
        expected_output = {
            'id': 1,
            'size': 4,
            'x': 5,
            'y': 2
        }
        self.assertEqual(s.to_dictionary(), expected_output)


class TestSquareToString(unittest.TestCase):
    """Unittests for __str__ method of the Square class"""

    def test_to_string_with_width_height(self):
        r = Square(4)
        expected_output = "[Square] ({}) 0/0 - 4".format(r.id)
        self.assertEqual(r.__str__(), expected_output)

    def test_to_string_with_width_height_x(self):
        r = Square(4, 1)
        expected_output = "[Square] ({}) 1/0 - 4".format(r.id)
        self.assertEqual(r.__str__(), expected_output)

    def test_to_string_with_width_height_x_y(self):
        r = Square(4, 1, 2)
        expected_output = "[Square] ({}) 1/2 - 4".format(r.id)
        self.assertEqual(r.__str__(), expected_output)

    def test_to_string_with_width_height_x_y_ID(self):
        r = Square(4, 1, 2, 9)
        expected_output = "[Square] (9) 1/2 - 4"
        self.assertEqual(r.__str__(), expected_output)


class TestSquareUpdate(unittest.TestCase):
    """Unittests for to_update method of the Square class"""

    def test_update_with_no_arguments(self):
        s = Square(4)
        s.update()
        obj = (s.id, s.size, s.x, s.y)
        self.assertEqual(obj, (s.id, 4, 0, 0))

    def test_update_with_one_argument(self):
        s = Square(4)
        s.update(9)
        obj = (s.id, s.size, s.x, s.y)
        self.assertEqual(obj, (9, 4, 0, 0))

    def test_update_with_two_arguments(self):
        s = Square(4)
        s.update(9, 3)
        obj = (s.id, s.size, s.x, s.y)
        self.assertEqual(obj, (9, 3, 0, 0))

    def test_update_with_three_arguments(self):
        s = Square(4)
        s.update(9, 3, 7)
        obj = (s.id, s.size, s.x, s.y)
        self.assertEqual(obj, (9, 3, 7, 0))

    def test_update_with_four_arguments(self):
        s = Square(4)
        s.update(9, 3, 7, 1)
        obj = (s.id, s.size, s.x, s.y)
        self.assertEqual(obj, (9, 3, 7, 1))

    def test_update_with_five_arguments(self):
        s = Square(4)
        s.update(9, 3, 7, 1, 1)
        obj = (s.id, s.width, s.x, s.y)
        self.assertEqual(obj, (9, 4, 7, 1))

    def test_update_one_kwargs(self):
        s = Square(4)
        s.update(id=89)
        obj = {
            'id': s.id,
            'size': s.width,
            'x': s.x,
            'y': s.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'size': 4,
            'x': 0,
            'y': 0
        })

    def test_update_two_kwargs(self):
        s = Square(4)
        s.update(id=89, size=7)
        obj = {
            'id': s.id,
            'size': s.size,
            'x': s.x,
            'y': s.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'size': 7,
            'x': 0,
            'y': 0
        })

    def test_update_three_kwargs(self):
        s = Square(4)
        s.update(id=89, size=7, x=2)
        obj = {
            'id': s.id,
            'size': s.size,
            'x': s.x,
            'y': s.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'size': 7,
            'x': 2,
            'y': 0
        })

    def test_update_four_kwargs(self):
        s = Square(4)
        s.update(id=89, size=7, x=2, y=3)
        obj = {
            'id': s.id,
            'size': s.size,
            'x': s.x,
            'y': s.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'size': 7,
            'x': 2,
            'y': 3
        })

    def test_update_five_kwargs(self):
        s = Square(4)
        s.update(id=89, size=7, x=2, y=3, a=1)
        obj = {
            'id': s.id,
            'size': s.size,
            'x': s.x,
            'y': s.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'size': 7,
            'x': 2,
            'y': 3
        })


if __name__ == '__main__':
    unittest.main()
