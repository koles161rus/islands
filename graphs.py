import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x50 = []
y50 = []
z50 = []
fig, ax = plt.subplots()

for i in range(10):
    x50.append(numpy.loadtxt('./d50/100x%s00.txt' % str(i + 1), usecols=[2], delimiter="\t"))
    y50.append(numpy.loadtxt('./d50/100x%s00.txt' % str(i + 1), usecols=[1], delimiter="\t"))
    z50.append(numpy.ones(100, dtype=int) * (i + 1))
    ax.scatter(z50[i], x50[i], s=1, c='blue')
    ax.scatter(z50[i], y50[i], s=1, c='red')

    if i == 0:
        ax.scatter(i + 1, numpy.mean(x50[i]), s=50, c='blue', label='по оси x')
        ax.scatter(i + 1, numpy.mean(y50[i]), s=50, c='red', label='по оси y')
    else:
        ax.scatter(i + 1, numpy.mean(x50[i]), s=50, c='blue')
        ax.scatter(i + 1, numpy.mean(y50[i]), s=50, c='red')

legend = ax.legend(loc="center right", title="Объёмные доли")
ax.add_artist(legend)

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))

ax.set_xlabel('l/d', fontsize=16)
ax.xaxis.set_label_coords(1.02, -0.02)
ax.set_ylabel('φ', rotation=0, fontsize=16)
ax.yaxis.set_label_coords(-0.04, 0.98)
plt.show()

x25 = []
y25 = []
z25 = []
fig, ax = plt.subplots()

for i in range(10):
    x25.append(numpy.loadtxt('./d25/100x%s00.txt' % str(i + 1), usecols=[2], delimiter="\t"))
    y25.append(numpy.loadtxt('./d25/100x%s00.txt' % str(i + 1), usecols=[1], delimiter="\t"))
    z25.append(numpy.ones(100, dtype=int) * (i + 1))
    ax.scatter(z25[i], x25[i], s=1, c='blue')
    ax.scatter(z25[i], y25[i], s=1, c='red')

    if i == 0:
        ax.scatter(i + 1, numpy.mean(x25[i]), s=50, c='blue', label='по оси x')
        ax.scatter(i + 1, numpy.mean(y25[i]), s=50, c='red', label='по оси y')
    else:
        ax.scatter(i + 1, numpy.mean(x25[i]), s=50, c='blue')
        ax.scatter(i + 1, numpy.mean(y25[i]), s=50, c='red')

legend = ax.legend(loc="center right", title="Объёмные доли")
ax.add_artist(legend)

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))

ax.set_xlabel('l/d', fontsize=16)
ax.xaxis.set_label_coords(1.02, -0.02)
ax.set_ylabel('φ', rotation=0, fontsize=16)
ax.yaxis.set_label_coords(-0.04, 1)
plt.show()

x12 = []
y12 = []
z12 = []
fig, ax = plt.subplots()

for i in range(10):
    x12.append(numpy.loadtxt('./d12.5/100x%s00.txt' % str(i + 1), usecols=[2], delimiter="\t"))
    y12.append(numpy.loadtxt('./d12.5/100x%s00.txt' % str(i + 1), usecols=[1], delimiter="\t"))
    z12.append(numpy.ones(100, dtype=int) * (i + 1))
    ax.scatter(z12[i], x12[i], s=1, c='blue')
    ax.scatter(z12[i], y12[i], s=1, c='red')

    if i == 0:
        ax.scatter(i + 1, numpy.mean(x12[i]), s=50, c='blue', label='по оси x')
        ax.scatter(i + 1, numpy.mean(y12[i]), s=50, c='red', label='по оси y')
    else:
        ax.scatter(i + 1, numpy.mean(x12[i]), s=50, c='blue')
        ax.scatter(i + 1, numpy.mean(y12[i]), s=50, c='red')

legend = ax.legend(loc="center right", title="Объёмные доли")
ax.add_artist(legend)

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))

ax.set_xlabel('l/d', fontsize=16)
ax.xaxis.set_label_coords(1.02, -0.02)
ax.set_ylabel('φ', rotation=0, fontsize=16)
ax.yaxis.set_label_coords(-0.04, 1)
plt.show()