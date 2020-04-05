from utils.intcode_computer import IntcodeComputer


class DailyPuzzle09:
    def __init__(self):
        self.data = None

    def read_data(self):
        # read input data
        with open("./d09/input.txt") as f:
            lines = f.readline().split(",")
            self.data = [int(line) for line in lines]

    def solve_part_one(self):
        program = self.data.copy()
        intcode_computer = IntcodeComputer(program, [1])
        intcode_computer.run_until_termination()
        return intcode_computer.outputs[0]

    def solve_part_two(self):
        program = self.data.copy()
        intcode_computer = IntcodeComputer(program, [2])
        intcode_computer.run_until_termination()
        return intcode_computer.outputs[0]
