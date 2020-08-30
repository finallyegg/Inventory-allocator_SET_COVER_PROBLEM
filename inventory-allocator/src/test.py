import unittest
import copy
from Warehouse import Warehouse
from solution1 import findCheapest_simple
from solution2 import findCheapest_complex


class TestSolution(unittest.TestCase):
    order1 = {"apple": 5, "banana": 6}
    order2 = {"apple": 10, "banana": 10}
    order3 = {"apple": 100, "banana": 10}

    w1 = Warehouse(name="a", inventory={"apple": 1, "banana": 2})
    w2 = Warehouse(name="b", inventory={"apple": 5, "banana": 6})
    w3 = Warehouse(name="c", inventory={"apple": 5, "banana": 6})
    w4 = Warehouse(name="d", inventory={"apple": 94, "banana": 97})
    w5 = Warehouse(name="e", inventory={})

    def test_simple(self):
        supply = copy.deepcopy([self.w1, self.w2])
        result = findCheapest_simple(self.order1, supply)
        self.assertEqual(result, [{'b': {'apple': 5, 'banana': 6}}])

    def test_simple_2(self):
        supply = copy.deepcopy([self.w1, self.w2, self.w3])
        result = findCheapest_simple(self.order2, supply)
        self.assertEqual(result, [{'a': {'apple': 1, 'banana': 2}}, {
                         'b': {'apple': 5, 'banana': 6}}, {'c': {'apple': 4, 'banana': 2}}])

    def test_simple_large(self):
        supply = copy.deepcopy([self.w1, self.w2, self.w3])
        result = findCheapest_simple(self.order3, supply)
        self.assertEqual(result, [])

    def test_simple_null_supply(self):
        supply = []
        result = findCheapest_simple(self.order3, supply)
        self.assertEqual(result, [])

    def test_simple_null_supply_2(self):
        supply = [self.w1, self.w5]
        result = findCheapest_simple(self.order2, supply)
        self.assertEqual(result, [])

    def test_simple_null_order(self):
        supply = copy.deepcopy([self.w1, self.w2, self.w3])
        result = findCheapest_simple({}, supply)
        self.assertEqual(result, [])

    def test_complex(self):
        supply = copy.deepcopy([self.w1, self.w2, self.w3])
        result = findCheapest_complex(self.order2, supply)
        self.assertEqual(result, [{'b': {'apple': 5, 'banana': 6}}, {
                         'c': {'apple': 5, 'banana': 4}}])

    def test_complex_1(self):
        supply = copy.deepcopy([self.w1, self.w2, self.w3, self.w4])
        result = findCheapest_complex(self.order3, supply)
        self.assertEqual(result, [{'a': {'apple': 1, 'banana': 2}}, {
                         'b': {'apple': 5, 'banana': 6}}, {'d': {'apple': 94, 'banana': 2}}])

    def test_complex_null_supply(self):
        supply = [self.w5]
        result = findCheapest_complex(self.order1, supply)
        self.assertEqual(result, [])

    def test_complex_null_order(self):
        supply = [self.w1, self.w5]
        result = findCheapest_complex({}, supply)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
