from utils.intcode_computer import IntcodeComputer


class DailyPuzzle02:
    def __init__(self):
        self.data = None

    def read_data(self):
        with open("./d02/input.txt") as f:
            tmp = f.readline().split(",")
            self.data = [int(i) for i in tmp]

    def solve_part_one(self):
        program = self.data.copy()
        program[1] = 12
        program[2] = 2

        intcode_computer = IntcodeComputer(program)
        intcode_computer.run_until_termination()
        return intcode_computer.intcode_program[0]

    def solve_part_two(self, noun, verb):
        program = self.data.copy()

        # inputs
        program[1] = noun
        program[2] = verb

        intcode_computer = IntcodeComputer(program)
        intcode_computer.run_until_termination()

        # check result
        if intcode_computer.intcode_program[0] == 19690720:
            return 100 * noun + verb
        else:
            return 0
