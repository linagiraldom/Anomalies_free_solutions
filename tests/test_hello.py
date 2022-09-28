import unittest
from anomalies_sol import Anomalies_free_solutions


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(Anomalies_free_solutions.hello(),
                         'Hello, World!', True)


if __name__ == '__main__':
    unittest.main()
