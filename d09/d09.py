class DailyPuzzle09:
    def __init__(self):
        self.data = None

    def read_data(self):
        # read input data
        with open("./d05/input.txt") as f:
            lines = f.readline().split(",")
            self.data = [int(line) for line in lines]

    def solve_part_one(self):
        return 0

    def solve_part_two(self):
        return 0
