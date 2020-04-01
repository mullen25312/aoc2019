import math


class DailyPuzzle01:
    def __init__(self):
        self.data = None

    def read_data(self):
        with open("./d01/input.txt") as f:
            lines = f.readlines()
            self.data = [int(line) for line in lines]

    def solve_part_one(self):
        return sum([max((math.floor(value / 3) - 2, 0)) for value in self.data])

    def solve_part_two(self):
        data = [max((math.floor(value / 3) - 2, 0)) for value in self.data]
        result = data
        while any(value != 0 for value in data):
            data = [max((math.floor(value / 3) - 2, 0)) for value in data]
            result = result + data
        return sum(result)
