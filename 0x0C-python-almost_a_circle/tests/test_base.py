import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):

    def test_base_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_base_with_none(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base2.id, base1.id + 1)

    def test_base_with_int(self):
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_base_with_str(self):
        base = Base('str')
        self.assertEqual(base.id, 'str')

    def test_base_with_float(self):
        base = Base(3.1)
        self.assertEqual(base.id, 3.1)

    def test_base_with_list(self):
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def test_base_with_tuple(self):
        base = Base((1,))
        self.assertEqual(base.id, (1,))

    def test_base_with_set(self):
        base = Base({1, 2})
        self.assertEqual(base.id, {1, 2})

    def test_base_with_dict(self):
        base = Base({'a': 1, 'b': 2})
        self.assertEqual(base.id, {'a': 1, 'b': 2})

    def test_base_with_bool(self):
        base = Base(False)
        self.assertEqual(base.id, False)

    def test_base_with_neg_int(self):
        base = Base(-1)
        self.assertEqual(base.id, -1)

    def test_base_with_zero(self):
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_base_with_complex_num(self):
        base = Base(complex(5, 7))
        self.assertEqual(base.id, complex(5, 7))

    def test_base_with_INF(self):
        base = Base(float('inf'))
        self.assertEqual(base.id, float('inf'))

    def test_base_with_neg_INF(self):
        base = Base(float('-inf'))
        self.assertEqual(base.id, float('-inf'))

    def test_base_with_large_num(self):
        base = Base(999999999999999999999999999999)
        self.assertEqual(base.id, 999999999999999999999999999999)

    def test_base_with_NAN(self):
        base = Base(float('nan'))
        self.assertNotEqual(base.id, float('nan'))

    def test_base_with_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):

    def test_to_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_with_None(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_of_dict(self):
        dict_list = [{"a": 5, "b": 10}, {"c": 1, "d": 2}]
        expected_str = "[{\"a\": 5, \"b\": 10}, {\"c\": 1, \"d\": 2}]"
        self.assertEqual(Base.to_json_string(dict_list), expected_str)

    def test_to_json_string_list_tuple(self):
        dict_list_of_tuple = [(5, 10), (1, 2)]
        expected_str = """[[5, 10], [1, 2]]"""
        self.assertEqual(Base.to_json_string(dict_list_of_tuple), expected_str)

    def test_to_json_string_list_set(self):
        dict_list_of_set = [(5, 10), {1, 2}]
        with self.assertRaises(TypeError):
            Base.to_json_string(dict_list_of_set)

    def test_to_json_string_list_to_dict_rect(self):
        r = Rectangle(10, 7, 2, 8, 7)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary), 53)

    def test_to_json_string_list_to_dict_square(self):
        s = Square(5, 1, 2, 8)
        dictionary = s.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_str = """[{"id": 8, "size": 5, "x": 1, "y": 2}]"""
        self.assertEqual(json_dictionary, expected_str)

    def test_to_json_with_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 2)


class TestBaseFromJsonString(unittest.TestCase):

    def test_from_json_string_with_no_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_with_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_with_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list_of_dict(self):
        json_list = "[{\"a\": 5, \"b\": 10}, {\"c\": 1, \"d\": 2}]"
        expected_list = [{"a": 5, "b": 10}, {"c": 1, "d": 2}]
        self.assertEqual(Base.from_json_string(json_list), expected_list)

    def test_from_json_string_list_of_list(self):
        json_list = """[[5, 10], [1, 2]]"""
        expected_list = [[5, 10], [1, 2]]
        self.assertEqual(Base.from_json_string(json_list), expected_list)

    def test_from_json_string_list_to_dict_rect(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(Base.from_json_string(json_dictionary), [dictionary])

    def test_from_json_string_list_to_dict_square(self):
        s = Square(5, 1, 2, 8)
        dictionary = s.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(Base.from_json_string(json_dictionary), [dictionary])

    def test_from_json_with_two_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(1, 2)


class TestBaseSaveToFile(unittest.TestCase):

    def tearDown(self) -> None:
        try:
            os.remove('Base.json')
        except IOError:
            pass
        try:
            os.remove('Rectangle.json')
        except IOError:
            pass
        try:
            os.remove('Square.json')
        except IOError:
            pass

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual(len(f.read()), 107)

    def test_save_to_file_square(self):
        s1 = Square(10, 1, 2, 8)
        s2 = Square(8, 1, 2, 6)
        Square.save_to_file([s1, s2])
        with open('Square.json', 'r') as f:
            self.assertEqual(len(f.read()), 77)

    def test_save_to_file_square_empty(self):
        Square.save_to_file([])
        with open('Square.json', 'r') as f:
            self.assertEqual(len(f.read()), 2)

    def test_save_to_file_two_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file(1, 2)


class TestBaseLoadFromFile(unittest.TestCase):

    def test_load_from_with_no_file(self):
        self.assertEqual(Base.load_from_file(), [])

    def test_load_from_load_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))

    def test_load_from_load_square(self):
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s1))

    def test_load_from_with_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(1)


class TestBaseSaveToFileCSV(unittest.TestCase):

    def tearDown(self) -> None:
        try:
            os.remove('Base.json')
        except IOError:
            pass
        try:
            os.remove('Rectangle.json')
        except IOError:
            pass
        try:
            os.remove('Square.json')
        except IOError:
            pass

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("id,size,x,y\n", f.read())

    def test_save_to_file_csv_empty_list(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual("id,width,height,x,y\n", f.read())

    def test_save_to_file_csv_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open('Rectangle.csv', 'r') as f:
            self.assertEqual(len(f.read()), 43)

    def test_save_to_file_csv_square(self):
        s1 = Square(10, 1, 2, 8)
        s2 = Square(8, 1, 2, 6)
        Square.save_to_file_csv([s1, s2])
        with open('Square.csv', 'r') as f:
            self.assertEqual(len(f.read()), 29)

    def test_save_to_file_csv_two_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv(1, 2)


class TestBaseLoadFromFileCSV(unittest.TestCase):

    def test_load_from_file_csv_with_no_file(self):
        self.assertEqual(Base.load_from_file(), [])

    def test_load_from_file_csv_load_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))

    def test_load_from_file_csv_load_square(self):
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(list_squares_output[0]), str(s1))

    def test_load_from_file_csv_with_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv(1)


class TestBaseCreate(unittest.TestCase):
    """Unittests for create methode of the Base class"""

    def test_create_with_no_arguments_rectangle(self):
        self.assertIsInstance(Rectangle.create(), Rectangle)

    def test_create_with_no_arguments_square(self):
        self.assertIsInstance(Square.create(), Square)

    def test_create_rectangle_equality_comparison(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_rectangle_str_comparison(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_create_square_equality_comparison(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_create_square_str_comparison(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))

    def test_create_square_with_two_args(self):
        with self.assertRaises(TypeError):
            Square.create(1, 2)

    def test_create_rectangle_with_two_args(self):
        with self.assertRaises(TypeError):
            Rectangle.create(1, 2)


if __name__ == '__main__':
    unittest.main()
