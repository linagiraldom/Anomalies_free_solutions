# Template for GitHub actions for DevOps

![Python package](https://github.com/restrepo/DevOps/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/restrepo/DevOps/workflows/Upload%20Python%20Package/badge.svg)

The related software just print `Hello World!`. To avoid conflicts with the package name, we use the Spanish translation _DesOper_

## Install
```bash
$ pip install -i https://test.pypi.org/simple/ Anomalies-free-solutions
```
## USAGE
```python
>>> from anomalies_sol import Anomalies_free_solutions
Anomalies_free_solutions.run(5)
       l         k                      z  gcd
0   [-2]   [-1, 2]     [2, 4, -7, -9, 10]    1
1    [4]   [-1, 2]   [4, 9, -14, -25, 26]    1
2    [1]  [-1, -5]  [2, 18, -23, -25, 28]    1
3   [-1]   [1, -4]      [1, 5, -7, -8, 9]    2
4    [5]   [-1, 2]   [5, 6, -12, -21, 22]    2
5    [5]  [-1, -2]   [5, 8, -14, -26, 27]    2
6    [1]   [-1, 6]  [1, 14, -17, -18, 20]    2
7    [1]   [2, -3]  [7, 13, -25, -27, 32]    2
8   [-3]   [-1, 4]   [7, 8, -17, -25, 27]    2
9    [5]    [1, 2]   [7, 9, -20, -22, 26]    2
10  [-6]   [-1, 2]   [7, 8, -18, -22, 25]    3
11   [1]   [3, -1]  [5, 11, -18, -26, 28]    3

```
Links:
* [Test pip page](https://test.pypi.org/project/desoper/)
* Flake8 Tool For Style Guide Enforcement
  * https://flake8.pycqa.org/ 
  * https://peps.python.org/pep-0008/
* [Test python code](https://docs.pytest.org/en/7.1.x/)
* [GitHub actions](https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions)
