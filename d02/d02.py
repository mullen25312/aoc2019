from utils.intcode_computer import IntcodeComputer


class DailyPuzzle:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d02/input.txt") as f:
            tmp = f.readline().split(",")
            self.data = [int(i) for i in tmp]

    def solve_part_one(self):
        data = self.data.copy()
        data[1] = 12
        data[2] = 2

        intcode_computer = IntcodeComputer(data)
        intcode_computer.run()
        return intcode_computer.return_intcode_program()[0]

    def solve_part_two(self, noun, verb):
        data = self.data.copy()

        # inputs
        data[1] = noun
        data[2] = verb

        intcode_computer = IntcodeComputer(data)
        intcode_computer.run()

        # check result
        if intcode_computer.return_intcode_program()[0] == 19690720:
            return 100 * noun + verb
        else:
            return 0
