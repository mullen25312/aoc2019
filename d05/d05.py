from utils.utils import IntcodeComputer


class DailyPuzzle:
    def __init__(self):
        self.data = [1002,4,3,4,33]

    def read_data(self):
        with open("./d05/input.txt") as f:
            tmp = f.readline().split(",")
            self.data = [int(i) for i in tmp]

    def solve_part_one(self):
        data = self.data.copy()

        intcode_computer = IntcodeComputer(data)
        intcode_computer.run()
        return True

    def solve_part_two(self):
        return True
