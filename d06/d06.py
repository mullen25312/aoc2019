from utils.tree import Tree


class DailyPuzzle06:
    def __init__(self):
        self.data = None

    def read_data(self):
        with open("./d06/input.txt") as f:
            lines = f.readlines()
            raw_data = [line.rstrip() for line in lines]

        # convert raw map data to dictionary for easy orbit indexing
        orbits = {line.split(")")[0]: [] for line in raw_data}
        for line in raw_data:
            orbits[line.split(")")[0]].append(line.split(")")[1])

        # store universal orbital map as tree in data
        self.data = Tree()
        self.data.add_child("COM")

        # parse raw map data to tree (non-recursively)
        nodes = [self.data]
        while nodes:
            for child in nodes[0].children:
                if child in orbits.keys():
                    for orbit in orbits[child]:
                        nodes[0].children[child].add_child(orbit)
                    nodes.append(nodes[0].children[child])
            nodes.pop(0)

    def solve_part_one(self):

        # universal_orbit_map.print_tree()
        return self.data.children["COM"].checksum()

    def solve_part_two(self):

        # find me (YOU) and santa (SAN)
        you = self.data.search_node("YOU")[2:]
        san = self.data.search_node("SAN")[2:]

        # determine common orbits
        both = [item for item in you if item in san]

        # distance is given by our distance w.r.t. COM minus twice the distance of smallest common orbit w.r.t. COM
        return (len(you) - 1) + (len(san) - 1) - 2 * len(both)
