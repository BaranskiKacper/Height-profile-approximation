def fill(rows, cols, value):
    matrix = []
    for r in range(0, rows):
        matrix.append([value for _ in range(0, cols)])
    return matrix


def factorization_LU(a, b):
    length = len(a)
    L = [[1 if x == y else 0 for x in range(length)] for y in range(length)]
    U = fill(length, length, 0)
    x = [1.0] * length
    y = [0] * length

    # Tworzymy macierze L i U, takie, że: LUx = b
    for i in range(length):
        for j in range(i + 1):
            U[j][i] += a[j][i]
            for k in range(j):
                U[j][i] -= L[j][k] * U[k][i]

        for j in range(i + 1, length):
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] += a[j][i]
            L[j][i] /= U[i][i]

    # Rozwiązujemy układ równań: Ly = b za pomocą podstawiania wprzód
    for j in range(length):
        value = b[j]
        for i in range(j):
            value -= L[j][i] * y[i]
        y[j] = value / L[j][j]

    # Rozwiązujemy układ równań: Ux = y za pomocą podstawiania wstecz
    for j in range(length - 1, -1, -1):
        value = y[j]
        for i in range(j + 1, length):
            value -= U[j][i] * x[i]
        x[j] = value / U[j][j]

    return x
