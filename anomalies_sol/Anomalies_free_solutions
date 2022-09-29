#!/usr/bin/env python3
r'''
Anomalies_free_solutions module
'''

from multiprocessing import Pool
from multiprocessing import cpu_count
import warnings
from anomalies import anomaly
import numpy as np
from itertools import permutations
from itertools import combinations_with_replacement
import pandas as pd
warnings.simplefilter('ignore')


# # Functions


def m_value(n):
    """
    Valor de `m` tanto para el caso par como impar

    Parameters
    ----------
    `n`: int, número de elementos en la solución

    Returns
    -------
    `m`: int, número de elementos en las listas l y k
    """
    if n % 2 == 0:
        m = n / 2 - 1
    else:
        m = (n - 3) / 2
    return int(m)


def all_comb_array(size, d_max):
    """
    A partir de un arreglo con los números [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    se crean arreglos de tamaño `size` que contengan todas
    las combinaciones posibles.

    Parameters
    ----------
    `size`: int, tamaño de los arreglos que se quieren crear
    `d_max`: int, número entero máximo para generar los arreglos,
    e.j., np.arange(-d_max,d_max)

    Returns
    -------
    `final_combinations`: list, lista de tuplas de listas con todas las
    combinaciones de tamaño `size`
    """

    lista = np.arange(-d_max, d_max + 1)

    """
    Creamos un arreglo con todas las combinaciones con reemplazo de tamaño dos
    con los objetos de lista. Si yo tengo el arreglo [1,2,3] la combinación
    con reemplazo me da la siguiente solución
    A = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    """
    all_combinations = list(combinations_with_replacement(lista, size))

    # La permutación de las anteriores combinaciones de A dan el
    # siguiente resultado:
    # array([[[1, 1],[1, 1]],  ----> Eliminamos luego uno de estos
    #        [[1, 2],[2, 1]],
    #        [[1, 3],[3, 1]],
    #        [[2, 2],[2, 2]],  ----> Eliminamos luego uno de estos
    #        [[2, 3],[3, 2]],
    #        [[3, 3],[3, 3]]]) ----> Eliminamos luego uno de estos
    perm = list(map(permutations, all_combinations))
    perm_list = np.array(list(map(list, perm)))
    shape = np.shape(perm_list)

    # Volvemos todas las combinaciones en un arreglo 1D
    perm_list_1D = np.reshape(perm_list, (shape[0] * shape[1], shape[2]))
    # Eliminamos los elementos repetidos
    final_combinations = [list(x) for x in set(tuple(x) for x in perm_list_1D)]
    return final_combinations


def l_and_k_arrays(n, d_max):
    """
    Genera arreglos para l y k dependiendo de `n` con los cuales se van a
    obtener las soluciones quirales

    Parameters
    ----------
    `n`: int, number of elements in the solution
    `d_max`: int, número entero máximo para generar los arreglos,
    e.j., np.arange(-d_max,d_max). Se usa en la función all_comb_array
    que es llamada internamente dentro de esta función

    Returns
    -------
    `all_combinations_lk`: list, lista de tuplas con las posibles combinaciones
    de l y k [(l1,k1),..]
    """
    m = m_value(n)

    l_dummy = all_comb_array(m, d_max)

    # Para el caso impar: l y k tienen dimensiones diferentes,
    # los combinamos diferente :P
    if n % 2 != 0:
        k_dummy = all_comb_array(m + 1, d_max)
        # print(len(l_dummy), len(k_dummy))

        all_combinations_lk = [(i, j) for i in l_dummy for j in k_dummy]

    # En el caso par: l y k tienen las mismas dimensiones
    else:
        all_combinations_lk = list(combinations_with_replacement(l_dummy, 2))

    return all_combinations_lk


def is_vectorlike_solution(solution):
    """
    Verifica si al menos existe un elemento con su opuesto, si es el caso
    entonces es vectorlike y se marca como true para ser descartado

    Parameters
    ----------
    `solution`: list, solución a la operación merger

    Returns
    -------
    `isvectorlike`: bool, regresa verdadero si es una solución vectorlike
    """
    solution = np.array(solution)
    # De la solución sacamos en valor absoluto los diferentes valores que hay
    values = np.unique(abs(solution))
    # Asumimos de entrada que no es vectorlike
    isvectorlike = False

    for zabs in values:
        # Si tenemos al menos una solución que contenga un cero ya decimos que
        # es vectorlike
        if zabs == 0:
            isvectorlike = True
            break

        # Miramos si para un valor está tanto su valor positivo como su
        # negativo, si es así: es vectorlike
        if -zabs in solution and zabs in solution:
            isvectorlike = True
            break
    return isvectorlike


def chiral_solution(vector):
    """
    Soluciones quirales para `n` mayor o igual a 5

    Parameters
    ----------
    `vector`: list, lista de listas que contiene a los vectores l y k

    Returns
    -------
    `dict_sol`: list, lista de diccionarios con todas las soluciones quirales
    (incluye repetidas). Tiene la estructura:
    dict_sol = [{'n':int, 'l': list, 'k':list, 'z': list, 'gcd':int}]
    """

    dict_sol = []

    anomaly.free(vector[0], vector[1])
    solution = anomaly.free.simplified
    gcd = anomaly.free.gcd

    if solution[0] < 0:
        solution = -solution
    # Verificamos que sea una solución quiral y la guardamos
    if is_vectorlike_solution(solution) is False:
        dict_sol += [{"l": vector[0], "k": vector[1],
                     "z": solution, "gcd": gcd}]

    return dict_sol


# # Quitando soluciones duplicadas


def unique_solutions(sols, save=False, zmax=32):
    """
    Mantiene las soluciones quirales únicas y si se requiere se
    guardan en un archivo json.

    Parameters
    ----------
    `sols`: list, lista que contienen las soluciones en formato diccionario
    `save`: bool, en caso de ser True guarda las soluciones.
    Por defecto es igual a False.
    `zmax`: int, número entero máximo en valor absoluto que puede contener las
    soluciones. Por defecto se tiene zmax=32.

    Returns
    -------
    `df`: dataframe, dataframe con las soluciones quirales únicas. Contiene las
    columnas l, k, z y gcd.
    """

    df = pd.DataFrame(sols)
    df.sort_values('gcd', inplace=True)
    df['zmax'] = df['z'].agg(lambda x: np.all(np.unique(abs(x)) <= zmax))
    df = df[df.zmax]
    df = df.drop('zmax', axis='columns').reset_index(drop=True)
    df['zs'] = df['z'].astype(str)
    df = df.drop_duplicates('zs')
    df = df.drop('zs', axis='columns').reset_index(drop=True)

    if save:
        n = df["n"].max()
        df.to_json(f"solution_{n}.json", orient="records")

    return df  # dataframe con soluciones quirales únicas


def eq_satisfied(x):
    """
    This function verifies that equations (z1³+z2³+ ... + zn³ = 0) and
    (z1+z2+ ... + zn = 0) are satisfied at the same time, and if it is
    true, then return the input parameters

    Parameters
    ----------
    `x`: it correspond to the solutions z1, z2, ..., zn

    Return
    ------
    `eq_3`: int, returns the result of evaluating the equations
    `eq_1`: int, returns the result of evaluating the equations
    """
    x = np.array(x)
    eq_3 = np.sum(x ** 3)
    eq_1 = np.sum(x)

    return eq_3, eq_1


def run(n, use=7, zmax=32, dmax=15):

    results = 0
    processes = cpu_count()  # Para saber cuántos procesadores tengo
    if use <= processes:
        pool = Pool(processes=use)
    else:
        pool = Pool()  # Usar todos por defecto

    # Calculando los z quirales
    vector_lk = l_and_k_arrays(n, dmax)
    results = pool.map(chiral_solution, vector_lk)
    pool.close()
    pool.join()

    results = [res[0] for res in results if res != []]
    df_sols = unique_solutions(results, zmax=zmax)
    return df_sols


if __name__ == '__main__':

    # # Multiprocessing

    n = int(
        input(
            "¿Hasta que valor de n quiere calcular las soluciones quirales?")
    )

    df_sols = run(n)
    print(df_sols)

    # # Veamos si todas las soluciones obtenidas son soluciones realmente

    for sols in df_sols["z"]:
        eq3, eq1 = eq_satisfied(sols)
        assert eq3 == 0 and eq1 == 0
