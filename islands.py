import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy

iters = 50
phi_x = ["phi_x"]
phi_y = ["phi_y"]
number = ["#"]

radius = 6.25
size_x = [0, 1000]
size_y = [0, 100]


def add_circle(ax, center):
    circle = Circle(center, radius=radius, color='blue', linewidth=None)
    ax.add_patch(circle)


def dist2d(p, q):
    distance = numpy.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
    return distance


def conduct(graph_arr, center, centers):
    for c in centers:
        if c != center:
            if dist2d(c, center) < 2 * radius:
                graph_arr[centers.index(c), centers.index(center)] = dist2d(c, center)
                plt.plot([c[0], center[0]], [c[1], center[1]], color='orange', linewidth=5)
            else:
                graph_arr[centers.index(c), centers.index(center)] = float('inf')


def min_distance(dist, queue):
    minimum = float('inf')
    min_index = -1

    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index


def print_path(parent, j):
    if parent[j] == -1:
        return
    print_path(parent, parent[j])


def print_solution(dist, parent, axis, ends):
    for i in range(0, len(dist)):
        if dist[i] != float('inf'):
            print_path(parent, i)
            if axis == 'x':
                for right in ends:
                    if i == right:
                        return 'x'
            else:
                for top in ends:
                    if i == top:
                        return 'y'


def dijkstra(graph, src, axis, ends):
    row = len(graph)
    col = len(graph[0])

    dist = [float('inf')] * row
    parent = [-1] * row
    dist[src] = 0

    queue = []
    for i in range(row):
        queue.append(i)

    while queue:
        u = min_distance(dist, queue)
        if u == -1:
            break
        queue.remove(u)

        for i in range(col):
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u

    return print_solution(dist, parent, axis, ends)


def get_area(graph_arr, n_circle, centers, ax):
    add_circle(ax, center=centers[0])

    for n in range(n_circle - 1):
        center = (random.uniform(size_x[0], size_x[1]),
                  random.uniform(size_y[0], size_y[1]))
        centers.append(center)
        add_circle(ax, center=centers[-1])

    for c in centers:
        conduct(graph_arr, c, centers)

    x_min = min(c[0] - radius for c in centers)
    x_max = max(c[0] + radius for c in centers)
    y_min = min(c[1] - radius for c in centers)
    y_max = max(c[1] + radius for c in centers)

    dx = (x_max - x_min) / size_x[1]
    dy = (y_max - y_min) / size_y[1]

    count = 0

    for r in range(size_y[1]):
        y = y_min + r * dy
        for c in range(size_x[1]):
            x = x_min + c * dx
            if 0 < y < size_y[1] and 0 < x < size_x[1]:
                if any((x - center[0]) ** 2 + (y - center[1]) ** 2 <= (radius ** 2)
                   for center in centers):
                    count += 1

    area = count * dx * dy

    return round(area / (size_y[1] * size_x[1]), 5)


def get_border_circles(centers):
    lefts = []
    rights = []
    bottoms = []
    tops = []

    for c in centers:
        if c[0] < radius:
            lefts.append(centers.index(c))
        if c[0] > size_x[1] - radius:
            rights.append(centers.index(c))
        if c[1] < radius:
            bottoms.append(centers.index(c))
        if c[1] > size_y[1] - radius:
            tops.append(centers.index(c))

    return [lefts, rights, bottoms, tops]


def print_fig(val, ax, fig, cur):
    ax.set_xlim(size_x)
    ax.set_ylim(size_y)
    ax.tick_params(colors=(0, 0, 0, 0))
    if cur == 'x_cur':
        ax.set_title('Радиус = {}, Объёмная доля = {}, По оси x'.format(radius, val))
    else:
        ax.set_title('Радиус = {}, Объёмная доля = {}, По оси y'.format(radius, val))

    fig.tight_layout()
    fig.show()


def percolation(graph_arr, val, cur, begins, ends):
    if cur == 'x_cur':
        x_cur_bool = False
        for left in begins:
            current = dijkstra(graph_arr, left, 'x', ends)
            if current == 'x':
                x_cur_bool = True

        if x_cur_bool:
            phi_x.append(val)
            return False
        else:
            return True

    if cur == 'y_cur':
        y_cur_bool = False
        for bottom in begins:
            current = dijkstra(graph_arr, bottom, 'y', ends)
            if current == 'y':
                y_cur_bool = True

        if y_cur_bool:
            phi_y.append(val)
            return False
        else:
            return True


class Islands:
    def __init__(self, n_circle, cur):
        self.n_circle = n_circle
        self.cur = cur
        self.graph_arr = numpy.zeros([self.n_circle, self.n_circle])
        self.centers = [(random.uniform(size_x[0], size_x[1]),
                         random.uniform(size_y[0], size_y[1]))]
        self.fig, self.ax = plt.subplots(1, 1, figsize=(100, 10))

    def implement(self):
        val = get_area(self.graph_arr, self.n_circle, self.centers, self.ax)
        # print_fig(val, self.ax, self.fig, self.cur)

        border_circles = get_border_circles(self.centers)
        if self.cur == 'x_cur':
            begins = border_circles[0]
            ends = border_circles[1]
        else:
            begins = border_circles[2]
            ends = border_circles[3]
        return percolation(self.graph_arr, val, self.cur, begins, ends)


for i in range(iters):
    y_n_circles = 20
    y_islands = Islands(y_n_circles, 'y_cur')
    break_loop_y = y_islands.implement()
    x_n_circles = 20
    x_islands = Islands(x_n_circles, 'x_cur')
    break_loop_x = x_islands.implement()
    if break_loop_y or break_loop_x:
        break

    number.append(i + 1)
    print(i + 1)


if len(number) == len(phi_y) == len(phi_x):
    numpy.savetxt('./d12.5/100x1000-1020.txt', numpy.c_[number, phi_y, phi_x], delimiter="\t", fmt="%s")
    f = open("./d12.5/100x1000-1020.txt", "a")
    f.write('\nPhi_y avg: ' + str(numpy.mean(phi_y[1:])))
    f.write('\nPhi_x avg: ' + str(numpy.mean(phi_x[1:])))
    f = open("./d12.5/100x1000-1020.txt", "r")
    print(f.read())
else:
    print('number', len(number))
    print('phi_y', len(phi_y))
    print('phi_x', len(phi_x))
