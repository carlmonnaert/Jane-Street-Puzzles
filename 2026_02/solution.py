import numpy as np
import sympy as sp

(a, b , c) = sp.var('a b c')
grid = np.full((13, 13), None, dtype=object)

grid[0,4] = 6*c - 4*b

grid[1,7] = 8 - b

grid[2,1] = (a ** b - 4)/(6*c + 1)
grid[2,3] = (b + c)/(c - 1)
grid[2,6] = b ** 2 - b/c
grid[2,8] = sp.sqrt(30 + a)/c
grid[2,10] = (a + b)/(c - 3 * a)

grid[3,4] = (b - 3 * a)/(a - c)
grid[3,7] = (8 * a - 2 * b)
grid[3,9] = b/(a - c)
grid[3,11] = (b + 9)/sp.sqrt(c - a)

grid[4,1] = 18 /(a * c + 1)
grid[4,5] = c ** b
grid[4,10] = (3 + b ** 2)/sp.sqrt(3 + 2 * c)

grid[5,3] = b/(a ** 2 - c ** 2)
grid[5,12] = sp.sqrt(a + 2)/a

grid[6,2] = a ** b - 12/a
grid[6,4] = 2 * c + c/a
grid[6,6] = 4 * a - 5 * b
grid[6,8] = c + 2 * a
grid[6,10] = b/(9 * a - 5 * c)

grid[7,0] = (b ** 3 + 2 * c)/(b + 2 * c)
grid[7,9] = b/(a - 1)

grid[8,2] = (c - b)/(2 * a)
grid[8,7] = b/(a - c)
grid[8,11] = (b + c)/(a - c)

grid[9,1] = sp.log(a, c)
grid[9,3] = (c ** 2 - b)/a
grid[9,5] = (b - 1) ** 2
grid[9,8] = sp.real_root(43 - a * c, 3)/a

grid[10,2] = (b - a)/(a - c)
grid[10,4] = 11 - b
grid[10,6] = (b - 2 * a)/(a - c)
grid[10,9] = (c + 3)/a
grid[10,11] = 8 * c - b/c

grid[11,5] = b ** 2

grid[12,8] = (2 ** b + 1)/(a * c)

values = []
for i in range(13):
    for j in range(i+1):
        values.append(i+1)
values = values[::-1]

def fill_grid(values, i, j , a , b , c):
    directions = []

    if 0 < i and grid[i-1, j] is None:
        directions.append((i-1, j))
    if 0 < j and grid[i, j-1] is None:
        directions.append((i, j-1))
    if i < 12 and grid[i+1, j] is None:
        directions.append((i+1, j))
    if j < 12 and grid[i, j+1] is None:
        directions.append((i, j+1))
    
    if not directions:
        return None