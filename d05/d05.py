from utils.intcode_computer import IntcodeComputer


class DailyPuzzle:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d05/input.txt") as f:
            tmp = f.readline().split(",")
            self.data = [int(i) for i in tmp]

    def solve_part_one(self):
        data = self.data.copy()

        intcode_computer = IntcodeComputer(data)
        intcode_computer.run()
        return "puzzle part 1 run"

    def solve_part_two(self):
        data = self.data.copy()
        # data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        # data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        # data = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        # data = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        # data = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        # data = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]

        intcode_computer = IntcodeComputer(data)
        intcode_computer.run()
        return "puzzle part 2 run"
