# מגישים:גל דרעי, רן דרעי
# 318466224,318466216
# Github:https://github.com/randeSCE/Numeric_Analysis01

import numpy as np

MAT_SIZE = 3


def get_mat_input():
    # Get a MAT_SIZE x MAT_SIZE matrix from the user
    # Does not check for correct input currently
    mat = []
    for i in range(MAT_SIZE):
        row = []
        r = input(f"Enter 3 numbers for row #{i}\n")
        r = r.split(" ")
        for j in range(len(r)):
            row.append(int(r[j]))
        mat.append(row)
    return np.array(mat, dtype=float)


def scale_row(mat, row, scalar, id_mat):
    # Scale the row and the id mat
    id_mat[row] *= scalar
    mat[row] *= scalar


def sub_row(mat, r1, r2, scalar, id_mat):
    # Subtract row from row with scalar from mat and id mat
    mat[r2] -= mat[r1] * scalar
    id_mat[r2] -= id_mat[r1] * scalar


def col_handle(mat, index, id_mat):
    # Scale the relevant row to 1
    if mat[index][index] != 1 and mat[index][index] != 0:
        scale_row(mat, index, 1 / mat[index][index], id_mat)

    # Apply gauss algorithm
    if mat[index][index] != 0:
        for i in range(len(mat)):
            if i != index and mat[i][index] != 0:
                sub_row(mat, index, i, mat[i][index], id_mat)


def max_norm(mat):
    sizes = []
    for row in range(len(mat)):
        sum = 0
        for col in range(len(mat[row])):
            sum += abs(mat[row][col])
        sizes.append(sum)
    return max(sizes)


def cond(mat, inv_mat):
    mnmat = max_norm(mat)
    mninv = max_norm(inv_mat)
    return mnmat * mninv


def main():
    mat = np.array([[1, -1, -2], [2, -3, -5], [-1, 3, 5]], dtype=float)
    mat_backup = mat.copy()
    id_mat = np.identity(len(mat))
    print(f'before gaus:\n{mat}')
    for i in range(len(mat)):
        col_handle(mat, i, id_mat)

    print(f'after gaus:\n{mat}')
    print(f'inv:\n{id_mat}')
    # inv = np.linalg.inv(mat_backup)
    # print(f'real inv:\n{inv}')
    print(f'cond:{cond(mat_backup, id_mat)}')


if __name__ == '__main__':
    main()
