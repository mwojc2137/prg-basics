import matplotlib.pyplot as plt
import math

x = []
for i in range (361):
    x.append(i)

y = []
for n in x:
    y.append(math.sin(math.radians(n)))

plt.plot(x,y)
plt.show()