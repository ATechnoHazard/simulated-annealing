import numpy as np
import matplotlib.pyplot as plt


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(a, b):
        return np.sqrt(np.abs(a.x - b.x) + np.abs(a.y - b.y))

    @staticmethod
    def get_total_distance(coords):
        dist = 0
        for first, second in zip(coords[:-1], coords[1:]):
            dist += Coordinate.get_distance(first, second)

        dist += Coordinate.get_distance(coords[0], coords[-1])
        return dist


if __name__ == '__main__':
    # Fill up the coordinates
    coords = []
    costs = []
    NUM_POINTS = 10
    NUM_ITERATIONS = 1000

    for i in range(NUM_POINTS):
        coords.append(Coordinate(np.random.uniform(), np.random.uniform()))

    # plot
    fig = plt.figure(figsize=(10, 5))
    fig.show()
    fig.canvas.draw()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    cost0 = Coordinate.get_total_distance(coords)

    T = 30
    factor = 0.99
    for i in range(NUM_ITERATIONS):
        print(i, 'cost =', cost0)
        costs.append(cost0)

        T *= factor
        for j in range(500):
            # exchange two coordinates, get new neigbour solution
            r1, r2 = np.random.randint(0, len(coords), size=2)

            temp = coords[r1]
            coords[r1] = coords[r2]
            coords[r2] = temp

            # get new cost
            cost1 = Coordinate.get_total_distance(coords)

            if cost1 < cost0:
                cost0 = cost1
            else:
                x = np.random.uniform()
                if x < np.exp((cost0 - cost1) / T):
                    cost0 = cost1
                else:
                    temp = coords[r1]
                    coords[r1] = coords[r2]
                    coords[r2] = temp

        ax1.plot(costs)

        # plot the result
        for first, second in zip(coords[:-1], coords[1:]):
            ax2.plot([first.x, second.x], [first.y, second.y], 'b')
        ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')

        for c in coords:
            ax2.plot(c.x, c.y, 'ro')
        fig.canvas.draw()
        ax1.cla()
        ax2.cla()
