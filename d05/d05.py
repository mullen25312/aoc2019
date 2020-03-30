from utils.utils import IntcodeComputer


class DailyPuzzle:
    def __init__(self):
        self.data = [1002, 4, 3, 4, 33]

    def read_data(self):
        with open("./d05/input.txt") as f:
            tmp = f.readline().split(",")
            self.data = [int(i) for i in tmp]

    def solve_part_one(self):
        data = self.data.copy()

        intcode_computer = IntcodeComputer(data)
        intcode_computer.run()
        # print(intcode_computer.return_intcode_program())
        return True

    def solve_part_two(self):
        data = self.data.copy()
        # data = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        # data = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        # data = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        # data = [3, 3, 1107, -1, 8, 3, 4, 3, 99]

        intcode_computer = IntcodeComputer(data)
        intcode_computer.run()
        return True
