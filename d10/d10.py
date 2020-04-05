from collections import OrderedDict


def in_line_of_sight(vec1, vec2):
    # only vectors in the same quadrant can be in line of sight
    if ((vec1[0] >= 0) == (vec2[0] >= 0)) and ((vec1[1] >= 0) == (vec2[1] >= 0)):
        # check for linear dependency
        if vec1[0] != 0 and vec2[0] != 0:
            if vec1[1] / vec1[0] == vec2[1] / vec2[0]:
                return True
        if vec1[0] == 0 and vec2[0] == 0:
            return True
        else:
            return False
    else:
        return False


class DailyPuzzle10:
    def __init__(self):
        self.astroid_map_dict = {}

    def read_data(self):
        # read input data
        with open("./d10/input_example5.txt") as f:
            lines = f.readlines()
            # and save as dictionary with astroid positions as keys
            for y, line in enumerate(lines):
                for x, pos in enumerate(line):
                    if pos == "#":
                        self.astroid_map_dict[(x, y)] = []

    def solve_part_one(self):
        # look through all astroids
        for astroid in self.astroid_map_dict:
            # order other astroids by distance w.r.t. considered astroid
            other_astroids = OrderedDict(
                sorted(
                    self.astroid_map_dict.items(),
                    key=lambda item: (item[0][0] - astroid[0]) ** 2
                    + (item[0][1] - astroid[1]) ** 2,
                )
            )
            # delete first astroid with distance zero because it is itself
            other_astroids.popitem(last=False)

            # go through all other astroids ordered by distance
            for other_astroid in other_astroids:
                # assume it is not blocked
                self.astroid_map_dict[astroid].append(other_astroid)

                # and check against all other already in line of sight
                vec1 = (other_astroid[0] - astroid[0], other_astroid[1] - astroid[1])
                for los_astroid in self.astroid_map_dict[astroid][:-1]:
                    vec2 = (los_astroid[0] - astroid[0], los_astroid[1] - astroid[1])
                    if in_line_of_sight(vec1, vec2):
                        # if in line of sight dismiss
                        self.astroid_map_dict[astroid].pop()
                        break

        # find astroid position with most line of sight astroids
        key_max = max(
            self.astroid_map_dict.keys(),
            key=(lambda astroid: len(self.astroid_map_dict[astroid])),
        )

        # return number of most line of sight astroids
        return len(self.astroid_map_dict[key_max])

    def solve_part_two(self):
        return 0
