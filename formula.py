import matplotlib.pyplot as plt
import numpy as np


class Column:
    def __init__(self, name):
        self.data = []
        self.name = name.capitalize()


file = open("data.csv")
line = file.readline().rstrip()
array = line.split(',')
assert(len(array) == 2)
x = Column(array[0])
y = Column(array[1])

for line in file:
    line = line.rstrip()
    array = line.split(',')
    assert(len(array) == 2)
    x.data.append(float(array[0]))
    y.data.append(float(array[1]))

n = len(x.data)
assert(len(y.data) == n)
sigma_X = sum(x.data)
sigma_Y = sum(y.data)
sigma_XX = sum(_ * _ for _ in x.data)
sigma_XY = sum(_ * y.data[i] for i, _ in enumerate(x.data))
c = (sigma_Y * sigma_XX - sigma_X * sigma_XY) / \
    ((n * sigma_XX) - sigma_X**2)
m = (n * sigma_XY - sigma_X * sigma_Y) / (n * sigma_XX - sigma_X**2)

print (m, c)

xMax = max(x.data)
yMax = max(y.data)
plt.title("Linear regression")
plt.xlabel(x.name)
plt.ylabel(y.name)
plt.plot(x.data, y.data, 'ro')
plt.axis([0, xMax, 0, yMax])
z = np.array([0, xMax])
plt.plot(z, c + z * m)

plt.show()
