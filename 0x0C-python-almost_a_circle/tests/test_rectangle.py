import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO

"""Define Unittests for Rectangle class"""


class TestRectangle(unittest.TestCase):
    """Unittests for the new instance of the Rectangle Class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_rectangle_with_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_with_one_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_with_2_arguments(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(20, 2)
        obj2 = [r2.id, r2.width, r2.height, r2.x, r2.y]
        expected_result = [r1.id + 1, 20, 2, 0, 0]
        self.assertEqual(obj2, expected_result)

    def test_rectangle_with_3_arguments(self):
        r1 = Rectangle(10, 2, 3)
        r2 = Rectangle(20, 2, 4)
        obj2 = [r2.id, r2.width, r2.height, r2.x, r2.y]
        expected_result = [r1.id + 1, 20, 2, 4, 0]
        self.assertEqual(obj2, expected_result)

    def test_rectangle_with_4_arguments(self):
        r1 = Rectangle(10, 2, 3, 3)
        r2 = Rectangle(20, 2, 4, 4)
        obj2 = [r2.id, r2.width, r2.height, r2.x, r2.y]
        expected_result = [r1.id + 1, 20, 2, 4, 4]
        self.assertEqual(obj2, expected_result)

    def test_rectangle_with_5_arguments(self):
        r = Rectangle(10, 2, 3, 3, 12)
        obj2 = [r.id, r.width, r.height, r.x, r.y]
        expected_result = [12, 10, 2, 3, 3]
        self.assertEqual(obj2, expected_result)

    def test_rectangle_with_more_than_5_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)


class TestRectangleWidth(unittest.TestCase):
    """Unittest for the width attribute of the Rectangle class"""

    def test_width_setter_getter(self):
        r = Rectangle(1, 2)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_width_with_large_number(self):
        r = Rectangle(99999999999999999, 52)
        self.assertEqual(r.width, 99999999999999999)

    def test_width_type_error_str(self):
        with self.assertRaises(TypeError):
            Rectangle('yousef', 10, 0, 0, 9)

    def test_width_type_error_float(self):
        with self.assertRaises(TypeError):
            Rectangle(3.5, 10, 0, 0, 9)

    def test_width_type_error_list(self):
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], 10, 0, 0, 9)

    def test_width_type_error_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle((1,), 10, 0, 0, 9)

    def test_width_type_error_set(self):
        with self.assertRaises(TypeError):
            Rectangle({1, 2}, 10, 0, 0, 9)

    def test_width_type_error_dict(self):
        with self.assertRaises(TypeError):
            Rectangle({'a': 1, 'b': 2}, 10, 0, 0, 9)

    def test_width_type_error_bool(self):
        with self.assertRaises(TypeError):
            Rectangle(True, 10, 0, 0, 9)

    def test_width_with_complex_number(self):
        with self.assertRaises(TypeError):
            Rectangle(complex(5, 7), 10, 0, 0, 9)

    def test_width_with_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 10, 0, 0, 9)

    def test_width_with_negative_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(float('-inf'), 10, 0, 0, 9)

    def test_width_with_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 10, 0, 0, 9)

    def test_width_with_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10, 0, 0, 9)


class TestRectangleHeight(unittest.TestCase):
    """Unittest for the height attribute of the Rectangle class"""

    def test_height_setter_getter(self):
        r = Rectangle(1, 2)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_height_with_large_number(self):
        r = Rectangle(52, 99999999999999999)
        self.assertEqual(r.height, 99999999999999999)

    def test_height_type_error_str(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 'yousef', 0, 0, 9)

    def test_height_type_error_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 3.5, 0, 0, 9)

    def test_height_type_error_list(self):
        with self.assertRaises(TypeError):
            Rectangle(10, [1, 2, 3], 0, 0, 9)

    def test_height_type_error_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(10, (1,), 0, 0, 9)

    def test_height_type_error_set(self):
        with self.assertRaises(TypeError):
            Rectangle(10, {1, 2}, 0, 0, 9)

    def test_height_type_error_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(10, {'a': 1, 'b': 2}, 0, 0, 9)

    def test_height_type_error_bool(self):
        with self.assertRaises(TypeError):
            Rectangle(10, True, 0, 0, 9)

    def test_height_with_complex_number(self):
        with self.assertRaises(TypeError):
            Rectangle(10, complex(5, 7), 0, 0, 9)

    def test_height_with_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(10, float('inf'), 0, 0, 9)

    def test_height_with_negative_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(10, float('-inf'), 0, 0, 9)

    def test_height_with_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -10, 0, 0, 9)

    def test_height_with_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0, 9)


class TestRectangleX(unittest.TestCase):
    """Unittest for the x attribute of the Rectangle class"""

    def test_x_setter_getter(self):
        r = Rectangle(1, 2)
        r.x = 10
        self.assertEqual(r.x, 10)

    def test_x_with_zero(self):
        r = Rectangle(10, 12, 0, 0, 9)
        self.assertEqual(r.x, 0)

    def test_x_with_large_number(self):
        r = Rectangle(5, 10, 99999999999999999)
        self.assertEqual(r.x, 99999999999999999)

    def test_x_type_error_str(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 'yousef', 0, 9)

    def test_x_type_error_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 3.5, 0, 9)

    def test_x_type_error_list(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, [1, 2, 3], 0, 9)

    def test_x_type_error_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, (1,), 0, 9)

    def test_x_type_error_set(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, {1, 2}, 0, 9)

    def test_x_type_error_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, {'a': 1, 'b': 2}, 0, 9)

    def test_x_type_error_bool(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, True, 0, 9)

    def test_x_with_complex_number(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, complex(5, 7), 0, 9)

    def test_x_with_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, float('inf'), 0, 9)

    def test_x_with_negative_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, float('-inf'), 0, 9)

    def test_x_with_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 12, -10, 0, 9)


class TestRectangleY(unittest.TestCase):
    """Unittest for the y attribute of the Rectangle class"""

    def test_y_setter_getter(self):
        r = Rectangle(1, 2)
        r.y = 10
        self.assertEqual(r.y, 10)

    def test_y_with_zero(self):
        r = Rectangle(10, 12, 1, 0, 9)
        self.assertEqual(r.y, 0)

    def test_y_with_large_number(self):
        r = Rectangle(5, 10, 0, 99999999999999999)
        self.assertEqual(r.y, 99999999999999999)

    def test_y_type_error_str(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 1, 'yousef', 9)

    def test_y_type_error_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 1, 3.5, 9)

    def test_y_type_error_list(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, [1, 2, 3], 9)

    def test_y_type_error_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, (1,), 9)

    def test_y_type_error_set(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, {1, 2}, 9)

    def test_y_type_error_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, {'a': 1, 'b': 2}, 9)

    def test_y_type_error_bool(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, True, 9)

    def test_y_with_complex_number(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, complex(5, 7), 9)

    def test_y_with_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, float('inf'), 9)

    def test_y_with_negative_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 1, float('-inf'), 9)

    def test_y_with_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 12, 1, -10, 9)


class TestRectangleArea(unittest.TestCase):
    """Unittests for area method of the Rectangle class"""

    def test_area_with_argument(self):
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5)
            r.area('str')

    def test_area_with_small_numbers(self):
        r = Rectangle(4, 5, 0, 0, 10)
        self.assertEqual(r.area(), 20)

    def test_area_with_large_numbers(self):
        r = Rectangle(99999999999999999, 99999999999999999, 0, 0, 10)
        self.assertEqual(r.area(), 9999999999999999800000000000000001)


class TestRectangleDisplay(unittest.TestCase):
    """Unittests for display method of the Rectangle class"""

    def test_display_with_arguments(self):
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5)
            r.display('str')

    def test_display_with_zer0_x_zero_y(self):
        r = Rectangle(4, 4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_zero_y(self):
        r = Rectangle(4, 4, 2, 0, 9)
        expected_output = "  ####\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_zero_x(self):
        r = Rectangle(4, 4, 0, 2, 9)
        expected_output = "\n\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x_y(self):
        r = Rectangle(4, 4, 1, 2, 9)
        expected_output = "\n\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)


class TestRectangleToDictionary(unittest.TestCase):
    """Unittest for to_dictionary method of the Rectangle class"""

    def test_to_dictionary_with_arguments(self):
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5)
            r.to_dictionary('str')

    def test_to_dictionary_Rectangle_with_2_arguments(self):
        r1 = Rectangle(10, 15)
        r2 = Rectangle(4, 5)
        expected_output = {
            'id': r1.id + 1,
            'width': 4,
            'height': 5,
            'x': 0,
            'y': 0
        }
        self.assertEqual(r2.to_dictionary(), expected_output)

    def test_to_dictionary_Rectangle_with_3_arguments(self):
        r1 = Rectangle(10, 15)
        r2 = Rectangle(4, 5, 2)
        expected_output = {
            'id': r1.id + 1,
            'width': 4,
            'height': 5,
            'x': 2,
            'y': 0
        }
        self.assertEqual(r2.to_dictionary(), expected_output)

    def test_to_dictionary_Rectangle_with_4_arguments(self):
        r1 = Rectangle(10, 15)
        r2 = Rectangle(4, 5, 2, 1)
        expected_output = {
            'id': r1.id + 1,
            'width': 4,
            'height': 5,
            'x': 2,
            'y': 1
        }
        self.assertEqual(r2.to_dictionary(), expected_output)

    def test_to_dictionary_Rectangle_with_5_arguments(self):
        r = Rectangle(4, 5, 2, 1, 9)
        expected_output = {
            'id': 9,
            'width': 4,
            'height': 5,
            'x': 2,
            'y': 1
        }
        self.assertEqual(r.to_dictionary(), expected_output)


class TestRectangleToString(unittest.TestCase):
    """Unittests for __str__ method of the Rectangle class"""

    def test_to_string_with_width_height(self):
        r = Rectangle(4, 6)
        expected_output = "[Rectangle] ({}) 0/0 - 4/6".format(r.id)
        self.assertEqual(r.__str__(), expected_output)

    def test_to_string_with_width_height_x(self):
        r = Rectangle(4, 6, 1)
        expected_output = "[Rectangle] ({}) 1/0 - 4/6".format(r.id)
        self.assertEqual(r.__str__(), expected_output)

    def test_to_string_with_width_height_x_y(self):
        r = Rectangle(4, 6, 1, 2)
        expected_output = "[Rectangle] ({}) 1/2 - 4/6".format(r.id)
        self.assertEqual(r.__str__(), expected_output)

    def test_to_string_with_width_height_x_y_ID(self):
        r = Rectangle(4, 6, 1, 2, 9)
        expected_output = "[Rectangle] (9) 1/2 - 4/6"
        self.assertEqual(r.__str__(), expected_output)


class TestRectangleUpdate(unittest.TestCase):
    """Unittests for to_update method of the Rectangle class """

    def test_update_with_no_arguments(self):
        r = Rectangle(4, 5)
        r.update()
        obj = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(obj, (r.id, 4, 5, 0, 0))

    def test_update_with_one_argument(self):
        r = Rectangle(4, 5)
        r.update(9)
        obj = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(obj, (9, 4, 5, 0, 0))

    def test_update_with_two_arguments(self):
        r = Rectangle(4, 5)
        r.update(9, 3)
        obj = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(obj, (9, 3, 5, 0, 0))

    def test_update_with_three_arguments(self):
        r = Rectangle(4, 5)
        r.update(9, 3, 7)
        obj = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(obj, (9, 3, 7, 0, 0))

    def test_update_with_four_arguments(self):
        r = Rectangle(4, 5)
        r.update(9, 3, 7, 1)
        obj = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(obj, (9, 3, 7, 1, 0))

    def test_update_with_five_arguments(self):
        r = Rectangle(4, 5)
        r.update(9, 3, 7, 1, 1)
        obj = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(obj, (9, 3, 7, 1, 1))

    def test_update_with_six_arguments(self):
        r = Rectangle(4, 5)
        r.update(9, 3, 7, 1, 1, 4)
        obj = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(obj, (9, 3, 7, 1, 1))

    def test_update_one_kwargs(self):
        r = Rectangle(4, 5)
        r.update(id=89)
        obj = {
            'id': r.id,
            'width': r.width,
            'height': r.height,
            'x': r.x,
            'y': r.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'width': 4,
            'height': 5,
            'x': 0,
            'y': 0
        })

    def test_update_two_kwargs(self):
        r = Rectangle(4, 5)
        r.update(id=89, height=7)
        obj = {
            'id': r.id,
            'width': r.width,
            'height': r.height,
            'x': r.x,
            'y': r.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'width': 4,
            'height': 7,
            'x': 0,
            'y': 0
        })

    def test_update_three_kwargs(self):
        r = Rectangle(4, 5)
        r.update(id=89, height=7, width=3)
        obj = {
            'id': r.id,
            'width': r.width,
            'height': r.height,
            'x': r.x,
            'y': r.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'width': 3,
            'height': 7,
            'x': 0,
            'y': 0
        })

    def test_update_four_kwargs(self):
        r = Rectangle(4, 5)
        r.update(id=89, height=7, width=3, x=2)
        obj = {
            'id': r.id,
            'width': r.width,
            'height': r.height,
            'x': r.x,
            'y': r.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'width': 3,
            'height': 7,
            'x': 2,
            'y': 0
        })

    def test_update_five_kwargs(self):
        r = Rectangle(4, 5)
        r.update(id=89, height=7, width=3, x=2, y=3)
        obj = {
            'id': r.id,
            'width': r.width,
            'height': r.height,
            'x': r.x,
            'y': r.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'width': 3,
            'height': 7,
            'x': 2,
            'y': 3
        })

    def test_update_six_kwargs(self):
        r = Rectangle(4, 5)
        r.update(id=89, height=7, width=3, x=2, y=3, a=1)
        obj = {
            'id': r.id,
            'width': r.width,
            'height': r.height,
            'x': r.x,
            'y': r.y
        }
        self.assertEqual(obj, {
            'id': 89,
            'width': 3,
            'height': 7,
            'x': 2,
            'y': 3
        })


if __name__ == '__main__':
    unittest.main()
