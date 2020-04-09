import math
import re
import numpy as np
from itertools import combinations

# positions of each coordinate in full vector
coordinates = {"x": 0, "y": 1, "z": 2}

# regular expression for parsing input
reg_expr = r"([xyz])=(-?\d+)"

# least common multiple based on greates common divisor
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def moons_difference_equation(moons):
    # split given state into positions and velocities
    dim = moons.shape[1] // 2
    pos = moons.copy()[:, 0:dim]
    vel = moons.copy()[:, dim : 2 * dim]

    # apply gravity
    n = pos.shape[0]
    # for each combination
    for pair in combinations(range(0, n), 2):
        # if moons position is greather than others position add -1 (1) to velocity
        vel[pair[0], np.greater(pos[pair[0], :], pos[pair[1], :])] -= 1
        vel[pair[1], np.greater(pos[pair[0], :], pos[pair[1], :])] += 1

        # if moons position is lesser than others position add 1 (-1) to velocity
        vel[pair[0], np.less(pos[pair[0], :], pos[pair[1], :])] += 1
        vel[pair[1], np.less(pos[pair[0], :], pos[pair[1], :])] -= 1

    # add velocity to position
    pos += vel

    # return stacked vector as next state
    return np.concatenate((pos, vel), axis=1)


def total_energy(moons):
    # split into positions and velocities
    dim = moons.shape[1] // 2
    pos = moons.copy()[:, 0:dim]
    vel = moons.copy()[:, dim : 2 * dim]

    # compute energies
    potential_energies = np.sum(np.absolute(pos), axis=1)
    kinetic_energies = np.sum(np.absolute(vel), axis=1)
    energies = np.multiply(potential_energies, kinetic_energies)

    # return sum of energies
    return sum(energies)


class DailyPuzzle12:
    def __init__(self):
        self.data = []

    def read_data(self):
        # read input data
        with open("./d12/input.txt") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                results = re.findall(reg_expr, line)
                self.data.append([0 for result in 2 * results])
                for result in results:
                    self.data[idx][coordinates[result[0]]] = int(result[1])

    def solve_part_one(self):
        steps = 1000  # number of steps
        moons = [np.array(self.data)]  # initial state

        # evaluate difference equation steps times
        for _ in range(0, steps):
            moons.append(moons_difference_equation(moons[-1]))

        # return total energy of last state
        return total_energy(moons[-1])

    def solve_part_two(self):
        # each coordinate is independent of each other
        # therefore find each axis cycle number

        # simulate for x-axis
        cnt_x = 1
        moons = [np.array(self.data)[:, [0, 3]]]
        moons.append(moons_difference_equation(moons[-1]))
        while not np.all(np.equal(moons[0], moons[-1])):
            moons.append(moons_difference_equation(moons[-1]))
            cnt_x += 1

        # simulate for y-axis
        cnt_y = 1
        moons = [np.array(self.data)[:, [1, 4]]]
        moons.append(moons_difference_equation(moons[-1]))
        while not np.all(np.equal(moons[0], moons[-1])):
            moons.append(moons_difference_equation(moons[-1]))
            cnt_y += 1

        # simulate for z-axis
        cnt_z = 1
        moons = [np.array(self.data)[:, [2, 5]]]
        moons.append(moons_difference_equation(moons[-1]))
        while not np.all(np.equal(moons[0], moons[-1])):
            moons.append(moons_difference_equation(moons[-1]))
            cnt_z += 1

        # overall cycle number is least common multiple of each axis cycle number
        return lcm(lcm(cnt_x, cnt_y), cnt_z)
