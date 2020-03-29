class d02:
    def __init__(self):
        self.data = []

    def read_data(self):
        with open("./d02/input.txt") as f:
            tmp = f.readline().split(",")
            self.data = [int(i) for i in tmp]

    def solve_part_one(self):
        data = self.data.copy()

        # inputs
        data[1] = 12
        data[2] = 2

        # run through opcodes
        idx = 0
        while data[idx] != 99 and idx <= len(data):

            # opcode 1
            if data[idx] == 1:
                data[data[idx + 3]] = data[data[idx + 1]] + data[data[idx + 2]]

            # opcode 2
            elif data[idx] == 2:
                data[data[idx + 3]] = data[data[idx + 1]] * data[data[idx + 2]]

            # next opcode
            idx = idx + 4

        return data[0]

    def solve_part_two(self, noun, verb):
        data = self.data.copy()

        # inputs
        data[1] = noun
        data[2] = verb

        # run through opcodes
        idx = 0
        while data[idx] != 99 and idx <= len(data):

            # opcode 1
            if data[idx] == 1:
                data[data[idx + 3]] = data[data[idx + 1]] + data[data[idx + 2]]

            # opcode 2
            elif data[idx] == 2:
                data[data[idx + 3]] = data[data[idx + 1]] * data[data[idx + 2]]

            # next opcode
            idx = idx + 4

        # check result
        if data[0] == 19690720:
            return 100 * noun + verb
        else:
            return 0
