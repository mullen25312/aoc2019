class IntcodeComputer:
    def __init__(self, intcode_program):
        self.opcodes = {
            1: self.addition_pos_pos,
            1001: self.addition_pos_imm,
            101: self.addition_imm_pos,
            1101: self.addition_imm_imm,
            2: self.mulitplication_pos_pos,
            1002: self.mulitplication_pos_imm,
            102: self.mulitplication_imm_pos,
            1102: self.mulitplication_imm_imm,
            3: self.input_pos,
            103: self.input_imm,
            4: self.output_pos,
            104: self.output_imm,
            99: self.terminate,
        }
        self.intruction_pointer = 0
        self.intcode_program = intcode_program

    def addition_pos_pos(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intcode_program[self.intruction_pointer + 1]]
            + self.intcode_program[self.intcode_program[self.intruction_pointer + 2]]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def addition_pos_imm(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intruction_pointer + 2]
            + self.intcode_program[self.intcode_program[self.intruction_pointer + 1]]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def addition_imm_pos(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intruction_pointer + 1]
            + self.intcode_program[self.intcode_program[self.intruction_pointer + 2]]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def addition_imm_imm(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intruction_pointer + 1]
            + self.intcode_program[self.intruction_pointer + 2]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def mulitplication_pos_pos(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intcode_program[self.intruction_pointer + 1]]
            * self.intcode_program[self.intcode_program[self.intruction_pointer + 2]]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def mulitplication_pos_imm(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intruction_pointer + 2]
            * self.intcode_program[self.intcode_program[self.intruction_pointer + 1]]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def mulitplication_imm_pos(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intruction_pointer + 1]
            * self.intcode_program[self.intcode_program[self.intruction_pointer + 2]]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def mulitplication_imm_imm(self):
        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            self.intcode_program[self.intruction_pointer + 1]
            * self.intcode_program[self.intruction_pointer + 2]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def input_pos(self):
        print("provide integer input: ")
        self.intcode_program[self.intcode_program[self.intruction_pointer + 1]] = int(
            input()
        )
        self.intruction_pointer = self.intruction_pointer + 2
        return True

    def input_imm(self):
        print("provide integer input: ")
        self.intcode_program[self.intruction_pointer + 1] = int(input())
        self.intruction_pointer = self.intruction_pointer + 2
        return True

    def output_pos(self):
        print(self.intcode_program[self.intcode_program[self.intruction_pointer + 1]])
        self.intruction_pointer = self.intruction_pointer + 2
        return True

    def output_imm(self):
        print(self.intcode_program[self.intruction_pointer + 1])
        self.intruction_pointer = self.intruction_pointer + 2
        return True

    def terminate(self):
        return False

    def return_intcode_program(self):
        return self.intcode_program

    def run(self):
        while self.opcodes[self.intcode_program[self.intruction_pointer]]() == True:
            pass
