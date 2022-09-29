#!/usr/bin/env python3

import unittest
from anomalies_sol import Anomalies_free_solutions


class Test_anomalies(unittest.TestCase):

    sols_n5 = Anomalies_free_solutions.run(5, zmax=30)
    sols_n6 = Anomalies_free_solutions.run(6, zmax=30)

    def test_n6_article_sol(self):
        # La lista [12, -11, -10, 8, 6, -5] es una solución dada por el
        # artículo. La ordenamos para ver si está en nuestras soluciones
        self.assertTrue(list(set(True for x in Test_anomalies.sols_n6['z']
                        if x.tolist() == [5, -6, -8, 10, 11, -12]))[0])

    def test_number_sols_n5(self):
        self.assertEqual(len(Test_anomalies.sols_n5), 11)

    def test_number_sols_n6(self):
        self.assertEqual(len(Test_anomalies.sols_n6), 112)

    # Verificación de las ecuaciones diofánticas para las soluciones quirales
    def test_suma_cubo(self):
        diophantic_eqs = list(map(Anomalies_free_solutions.eq_satisfied,
                                  Test_anomalies.sols_n5['z']))
        self.assertEqual(sum(list(map(sum, diophantic_eqs))), 0)


if __name__ == '__main__':
    unittest.main()
