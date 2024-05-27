import unittest
from sorter import Sorter


class Object:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} ({self.age})'

    def __eq__(self, other):
        if isinstance(other, Object):
            return self.name == other.name and self.age == other.age
        return False


class TestSorter(unittest.TestCase):
    SORT_METHODS = [
        ('bubble', Sorter.bubble_sort),
        ('insertion', Sorter.insertion_sort),
        ('quick', Sorter.quick_sort),
        ('merge', Sorter.merge_sort)
    ]

    def test_sort_numbers(self):
        arr = [5, 2, 8, 3, 1]
        expected = [1, 2, 3, 5, 8]
        for name, method in self.SORT_METHODS:
            with self.subTest(name=name):
                method(arr)
                self.assertEqual(arr, expected)

    def test_sort_strings(self):
        arr = ['абрикос', 'волк', 'барбос', 'авиатор']
        expected = ['абрикос', 'авиатор', 'барбос', 'волк']
        for name, method in self.SORT_METHODS:
            with self.subTest(name=name):
                method(arr)
                self.assertEqual(arr, expected)

    def test_sort_objects(self):
        people = TestSorter.create_object()
        expected = TestSorter.create_object(sorted=True)
        for name, method in self.SORT_METHODS:
            with self.subTest(name=name):
                method(people, key=lambda x: x.age)
                self.assertEqual(people, expected)
    @staticmethod
    def create_object(sorted=False):
        people = [
            Object('Люся', 25),
            Object('Вася', 30),
            Object('Петя', 20)
        ]
        if sorted:
            people.sort(key=lambda x: x.age)
        return people


if __name__ == '__main__':
    unittest.main()