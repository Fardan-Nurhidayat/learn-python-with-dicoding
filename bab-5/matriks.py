import numpy as np
matriks = [[0 for j in range(3)] for k in range(4)]
print(matriks)


matriks_np = np.array(matriks)
print(matriks_np)

matriks_np[0, 0] = 99
first_row_first_col = matriks_np[0, 0]
print(first_row_first_col)
