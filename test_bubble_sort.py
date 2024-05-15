import unittest
from sorter import Sorter


class TestBubbleSort(unittest.TestCase):
    def test_sort_numbers(self):
        arr = [5, 2, 8, 3, 1]
        expected = [1, 2, 3, 5, 8]
        Sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_sort_strings(self):
        arr = ['абрикос', 'волк', 'барбос', 'авиатор']
        expected = ['абрикос', 'авиатор', 'барбос', 'волк']
        Sorter.bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_sort_objects(self):
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __repr__(self):
                return f'{self.name} ({self.age})'

            def __eq__(self, other):
                if isinstance(other, Person):
                    return self.name == other.name and self.age == other.age
                return False

        people = [Person('Люся', 25), Person('Вася', 30), Person('Петя', 20)]
        expected = [Person('Петя', 20), Person('Люся', 25), Person('Вася', 30)]
        Sorter.bubble_sort(people, key=lambda x: x.age)
        self.assertEqual(people, expected)


if __name__ == '__main__':
    unittest.main()