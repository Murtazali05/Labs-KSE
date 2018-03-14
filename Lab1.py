
import numpy as np
import matplotlib.pyplot as plt

z0 = 0.0  # m
v0 = 500.0  # m/sec
g = 9.8  # m/sec^2
tm = 110.0  # sec


def speed(t):
    global g, v0
    return v0 - g * t

def way(t):
    global g, z0, v0
    return z0 + v0 * t - g * (t * t / 2)

nt = 1000  # размер массива
t = np.linspace(0., tm, nt)
v = [speed(i) for i in t]
z = [way(i) for i in t]

print("len(z)=", len(z))

# Simple calculation of Tflight
for i in range(len(z)):
    if z[i] < 0.0:
        Tflight = (t[i] + t[i - 1]) / 2.0
        print("Node of landing:", i)
        print("Tflight=", Tflight)
        break

tmax = v0 / g
print("Максимальная высота подъема: ", way(tmax))

plt.plot(t, v, 'r-', linewidth=3)
plt.plot(t, [0.0] * nt, 'g-', linewidth=1)
plt.axis([0, Tflight + 1, -500., 500.])
plt.grid(True)
plt.xlabel("t")
plt.ylabel("v(t)")
plt.savefig("v.png", dpi=300)
plt.show()

plt.plot(t, z, 'b-', linewidth=3)
plt.axis([0, Tflight + 1., 0., 14000.])
plt.grid(True)
plt.xlabel("t")
plt.ylabel("z(t)")
plt.savefig("z.png", dpi=300)
plt.show()