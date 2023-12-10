import numpy as np

def lagrange_interpolation(y, x_pred):
    y_pred = 0
    x = list(range(len(y)))
    for xj, yj in enumerate(y):
        x_tilde = np.array([x[:xj] + x[xj+1:]])
        y_pred += yj * np.prod((x_pred - x_tilde) / (xj - x_tilde))
    return y_pred

with open("input", "r") as file:
    sum = 0
    for line in file:
        y = np.array([int(token) for token in line.split()])
        x = np.array(range(len(y)))
        print("x", x)
        print("y", y)
        res = lagrange_interpolation(y, len(y))
        sum += round(res)
        print("Next:", res, round(res))
        print()
    print("Sum:", sum)