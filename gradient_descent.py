import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
assert(len(data.columns) == 2)
X = data.iloc[:, 0]

# Data normalization in order to avoid potential overflow
X_Max = np.max(X)
X_Min = np.min(X)

limit = max(X_Max, abs(X_Min))
X_Norm = X / limit

Y = data.iloc[:, 1]
Y_Max = np.max(Y)

m = 0
c = 0
L = 0.1
n = float(len(X))
assert(len(Y) == n)

it = 2200
for _ in range(it):
    Y_Pred = m * X_Norm + c
    m = m - L * (sum((Y_Pred - Y) * X_Norm) / n)
    c = c - L * (sum(Y_Pred - Y) / n)

m /= limit
# print sum((Y - (m * X + c)) ** 2) / n


def displayPrecision():
    Sig_X = sum(X)
    Sig_Y = sum(Y)
    Sig_XX = sum(_ * _ for _ in X)
    Sig_XY = sum(_ * Y[i] for i, _ in enumerate(X))
    __c = (Sig_Y * Sig_XX - Sig_X * Sig_XY) / ((n * Sig_XX) - Sig_X ** 2)
    __m = (n * Sig_XY - Sig_X * Sig_Y) / (n * Sig_XX - Sig_X ** 2)
    D_M = abs((m - __m) / __m * 100)
    D_C = abs((c - __c) / __c * 100)
    print "The algorithm precision (similarity with the result given by the close end formula for a simple linear regression) is {:.2f}%.".format(
        max(100 - (D_M + D_C) / 2, 0))


displayPrecision()
# Write fo file

plt.title("Linear regression")
plt.xlabel(data.columns[0].capitalize())
plt.ylabel(data.columns[1].capitalize())
plt.scatter(X, Y, color="red")
Z = np.array([X_Min, X_Max])
plt.plot(Z, m * Z + c)
plt.show()
