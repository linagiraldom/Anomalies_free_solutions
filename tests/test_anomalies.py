import unittest
from anomalies_sol import Anomalies_free_solutions

class Test_hello(unittest.TestCase):
    def test__n6(self):
        s6 = Anomalies_free_solutions.chiral_solution(6)
        self.assertEqual(s6, s6 | [5, -4, -4, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()