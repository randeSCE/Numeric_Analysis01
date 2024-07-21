# מגישים:גל דרעי, רן דרעי, ליאור אנגל
# 318466224,318466216,315006783
# Github:https://github.com/randeSCE/Numeric_Analysis01

import numpy as np

MAT_SIZE = 3
u_mats = []


def get_mat_input():
    # Get a MAT_SIZE x MAT_SIZE matrix from the user
    # Does not check for correct input currently
    mat = []
    print("Enter A:")
    for i in range(MAT_SIZE):
        row = []
        r = input(f"Enter 3 numbers for row #{i}\n")
        r = r.split(" ")
        for j in range(len(r)):
            row.append(int(r[j]))
        mat.append(row)
    return np.array(mat, dtype=float)


def sub_row(mat, r1, r2, scalar):
    # Subtract row from row with scalar from mat and id mat
    mat[r2] = mat[r2] - mat[r1] * scalar

    id_mat = np.identity(MAT_SIZE)
    id_mat2 = np.identity(MAT_SIZE)

    id_mat[r2][r1] = scalar
    id_mat2[r2][r1] = scalar

    u_mats.append(id_mat)


def pivot(mat, row):
    for i in range(row + 1, len(mat)):
        scalar = mat[i][row] / mat[row][row]
        sub_row(mat, row, i, scalar)


def LU(mat):
    for i in range(len(mat) - 1):
        pivot(mat, i)

    u = mat
    l = np.identity(MAT_SIZE)
    for i in range(len(u_mats)):
        l += u_mats[i]
    l -= np.identity(MAT_SIZE) * len(u_mats)



    return l, u


def main():
    A = np.array([[1, 4, -3], [-2, 1, 5], [3, 2, 1]], dtype=float)
    b = np.array([1, 2, 3], dtype=float)
    a = A.copy()
    l, u = LU(A)
    l_inv = np.linalg.inv(l)
    u_inv = np.linalg.inv(u)
    y = np.matmul(l_inv, b)
    x = np.matmul(u_inv, y)
    print(f'A:\n{a}')
    print(f'b:\n{b}')
    print(f'U:\n{u}')
    print(f'L:\n{l}')
    # print(f'our a:\n{np.matmul(l, u)}')
    print(f'x:{x}')



if __name__ == '__main__':
    main()
