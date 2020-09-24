import unittest


class TestMyBigModuleMethods(unittest.TestCase):

    # @unittest.skip(reason='Instead of using requests.get we will mock it.')
    def test_requests_get(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
