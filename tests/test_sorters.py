import unittest
import soreters as sorters


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
        ('bubble', sorters.BubleSort),
        ('insertion', sorters.InsertionSort),
        ('quick', sorters.QuickSort),
        ('merge', sorters.MergeSort)
    ]

    def __with_test(self, arr, expected, key=None):
        for name, sorter_class in self.SORT_METHODS:
            with self.subTest(name=name):
                sorter_class.sort(arr, key=key)
                self.assertEqual(arr, expected)

    @staticmethod
    def __create_objects(sorted_flag=False):
        people = [
            Object('Люся', 25),
            Object('Вася', 30),
            Object('Петя', 20)
        ]
        if sorted_flag:
            people.sort(key=lambda x: x.age)
        return people

    def test_with_types(self):
        data = [
            ([5, 2, 8, 3, 1], [1, 2, 3, 5, 8]),
            (['абрикос', 'волк', 'барбос', 'авиатор'],
             ['абрикос', 'авиатор', 'барбос', 'волк']),
        ]
        [self.__with_test(*data_type) for data_type in data]
        objects = (self.__create_objects(),
                   self.__create_objects(sorted_flag=True))
        self.__with_test(*objects, key=lambda x: x.age)
