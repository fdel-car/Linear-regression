import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
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
L = 0.02
n = len(X)
assert(len(Y) == n)

it = 10000
for _ in range(it):
    # while True:
    Y_Pred = m * X_Norm + c
    D_M = (-2.0 / n) * sum(X_Norm * (Y - Y_Pred))
    D_C = (-2.0 / n) * sum(Y - Y_Pred)
    m = m - L * D_M
    c = c - L * D_C
    # print D_M
    # if (abs(D_M) < 0.04):
    # break

m /= limit
print (m, c)
plt.title("Linear regression")
plt.scatter(X, Y, color="red")
Z = np.array([X_Min, X_Max])
plt.plot(Z, c + Z * m)
plt.show()
