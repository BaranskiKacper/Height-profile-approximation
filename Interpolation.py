from FactorizationLU import factorization_LU, fill


def lagrange(dis: list, height: list, x: float) -> float:
    Fx = 0.0
    for i in range(len(dis)):
        # Compute individual terms of above formula
        fi = 1
        for j in range(len(dis)):
            if j != i:
                fi = fi * (x - dis[j]) / (dis[i] - dis[j])
        # Add current term to result
        Fx = Fx + height[i] * fi
    return Fx


def splain_params(dis: list, height: list):
    n = len(dis)
    length = 4 * (n - 1)
    A = fill(length, length, 0.0)
    b = [0.0] * length

    #  Si(xj) = f(xj)
    for i in range(n - 1):
        row = [0] * length
        row[4 * i + 3] = 1
        A[4 * i + 3] = row
        b[4 * i + 3] = float(height[i])

    # Sj(Xj+1) = f(Xj+1)
    for i in range(n - 1):
        h = float(dis[i + 1]) - float(dis[i])
        row = [0.0] * length
        row[4 * i] = pow(h, 3)
        row[4 * i + 1] = pow(h, 2)
        row[4 * i + 2] = pow(h, 1)
        row[4 * i + 3] = 1
        A[4 * i + 2] = row
        b[4 * i + 2] = float(height[i + 1])

    # Sj-1'(xj) = Sj'(xj)
    for i in range(n - 2):
        h = float(dis[i + 1]) - float(dis[i])
        row = [0.0] * length
        row[4 * i] = 3 * pow(h, 2)
        row[4 * i + 1] = 2 * h
        row[4 * i + 2] = 1
        row[4 * (i + 1) + 2] = -1
        A[4 * i] = row
        b[4 * i] = 0.0

    # Sj-1''(xj) = Sj''(xj)
    for i in range(n - 2):
        h = dis[i + 1] - dis[i]
        row = [0.0] * length
        row[4 * i] = 6 * h
        row[4 * i + 1] = 2
        row[4 * (i + 1) + 1] = -2
        A[4 * (i + 1) + 1] = row
        b[4 * (i + 1) + 1] = 0.0

    # S0''(x0) = 0
    row = [0.0] * length
    row[1] = 2
    A[1] = row
    b[1] = 0.0

    # Sn-1''(xn-1) = 0
    row = [0.0] * length
    h = float(dis[-1]) - float(dis[-2])
    row[1] = 2
    row[-4] = 6 * h
    A[-4] = row
    b[-4] = 0.0

    params = factorization_LU(A, b)
    params4 = [params[i:i + 4] for i in range(0, len(params), 4)]
    return params4


def splain(dis: list, x: float, params4: list):
    for i in range(1, len(dis)):
        if float(dis[i - 1]) <= x <= float(dis[i]):
            h = x - float(dis[i - 1])
            a, b, c, d = params4[i - 1]
            return a * pow(h, 3) + b * pow(h, 2) + c * h + d
