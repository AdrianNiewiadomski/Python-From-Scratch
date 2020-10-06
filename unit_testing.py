import unittest
from my_big_module import calculate_sum as my_sum


class TestMyBigModuleMethods(unittest.TestCase):

    def test_calculate_sum(self):
        self.assertEqual(my_sum(2, 2), 4)

    def test_calculate_sum_incorrect(self):
        self.assertNotEqual(my_sum(2, -2), 1)

    def test_calculate_sum_error(self):
        with self.assertRaises(TypeError):
            my_sum(2, 'Marry')


if __name__ == '__main__':
    unittest.main()
