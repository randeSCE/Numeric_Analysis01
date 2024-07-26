# מגישים:גל דרעי, רן דרעי, ליאור אנגל
# 318466224,318466216,315006783
# Github:https://github.com/randeSCE/Numeric_Analysis01

import numpy as np

MAT_SIZE = 3


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


def is_dom_diag(mat: np.array):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j and mat[i][j] == 0:
                return False
    return True


def within_ep(x1, y1, z1, x2, y2, z2, ep):
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    z_diff = abs(z2 - z1)
    if x_diff < ep and y_diff < ep and z_diff < ep:
        return True
    return False


def yakobi(mat, b, ep):
    x, y, z = 0, 0, 0
    counter = 0
    while True:
        counter += 1
        x_r = float((b[0] - mat[0][1] * y - mat[0][2] * z) / mat[0][0])
        y_r = float((b[1] - mat[1][0] * x - mat[1][2] * z) / mat[1][1])
        z_r = float((b[2] - mat[2][0] * x - mat[2][1] * y) / mat[2][2])
        if within_ep(x, y, z, x_r, y_r, z_r, ep):
            x = x_r
            y = y_r
            z = z_r
            break

        x = x_r
        y = y_r
        z = z_r

    return x, y, z


def gauss_zaidel(mat, b, ep):
    x, y, z = 0, 0, 0
    counter = 0
    while True:
        counter += 1
        x_r = float((b[0] - mat[0][1] * y - mat[0][2] * z) / mat[0][0])
        y_r = float((b[1] - mat[1][0] * x_r - mat[1][2] * z) / mat[1][1])
        z_r = float((b[2] - mat[2][0] * x_r - mat[2][1] * y_r) / mat[2][2])
        if within_ep(x, y, z, x_r, y_r, z_r, ep):
            x = x_r
            y = y_r
            z = z_r
            break

        x = x_r
        y = y_r
        z = z_r

    return x, y, z


def main():
    mat = np.array([[4, 2, 0], [2, 10, 4], [0, 4, 5]])
    b = np.array([2, 6, 5])
    epsilon = 0.001
    print(f'matrix:\n{mat}\nb:{b}\nepsilon:{epsilon}')
    if not is_dom_diag(mat):
        print("Matrix does not have dominant diagonal!")
        return

    print(f"gauss zaidel solution:{gauss_zaidel(mat, b, epsilon)}")
    print(f"yakobi solution:{yakobi(mat, b, epsilon)}")


if __name__ == '__main__':
    main()
