import unittest
from my_big_module import calculate_sum as my_sum


class TestMyBigModuleMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass method has been called.')

    @classmethod
    def setUp(cls) -> None:
        print('setUp method has been called.')

    @classmethod
    def tearDown(cls) -> None:
        print('tearDown method has been called.')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass method has been called.')

    def test_calculate_sum(self):
        self.assertEqual(my_sum(2, 2), 4)

    def test_calculate_sum_incorrect(self):
        self.assertNotEqual(my_sum(2, -2), 1)


if __name__ == '__main__':
    unittest.main()
