param_modes = {"pos_mode": 0, "immediate_mode": 1}


class IntcodeComputer:
    def __init__(self, intcode_program):
        self.opcodes = {
            1: (self.addition, (param_modes["pos_mode"], param_modes["pos_mode"])),
            1001: (
                self.addition,
                (param_modes["pos_mode"], param_modes["immediate_mode"]),
            ),
            101: (
                self.addition,
                (param_modes["immediate_mode"], param_modes["pos_mode"]),
            ),
            1101: (
                self.addition,
                (param_modes["immediate_mode"], param_modes["immediate_mode"]),
            ),
            2: (
                self.mulitplication,
                (param_modes["pos_mode"], param_modes["pos_mode"]),
            ),
            1002: (
                self.mulitplication,
                (param_modes["pos_mode"], param_modes["immediate_mode"]),
            ),
            102: (
                self.mulitplication,
                (param_modes["immediate_mode"], param_modes["pos_mode"]),
            ),
            1102: (
                self.mulitplication,
                (param_modes["immediate_mode"], param_modes["immediate_mode"]),
            ),
            3: (self.input, (param_modes["pos_mode"],)),
            103: (self.input, (param_modes["immediate_mode"],)),
            4: (self.output, (param_modes["pos_mode"],)),
            104: (self.output, (param_modes["immediate_mode"],)),
            5: (self.jump_if_true, (param_modes["pos_mode"], param_modes["pos_mode"]),),
            1005: (
                self.jump_if_true,
                (param_modes["pos_mode"], param_modes["immediate_mode"]),
            ),
            105: (
                self.jump_if_true,
                (param_modes["immediate_mode"], param_modes["pos_mode"]),
            ),
            1105: (
                self.jump_if_true,
                (param_modes["immediate_mode"], param_modes["immediate_mode"]),
            ),
            6: (
                self.jump_if_false,
                (param_modes["pos_mode"], param_modes["pos_mode"]),
            ),
            1006: (
                self.jump_if_false,
                (param_modes["pos_mode"], param_modes["immediate_mode"]),
            ),
            106: (
                self.jump_if_false,
                (param_modes["immediate_mode"], param_modes["pos_mode"]),
            ),
            1106: (
                self.jump_if_false,
                (param_modes["immediate_mode"], param_modes["immediate_mode"]),
            ),
            7: (self.less_than, (param_modes["pos_mode"], param_modes["pos_mode"]),),
            1007: (
                self.less_than,
                (param_modes["pos_mode"], param_modes["immediate_mode"]),
            ),
            107: (
                self.less_than,
                (param_modes["immediate_mode"], param_modes["pos_mode"]),
            ),
            1107: (
                self.less_than,
                (param_modes["immediate_mode"], param_modes["immediate_mode"]),
            ),
            8: (self.equals, (param_modes["pos_mode"], param_modes["pos_mode"]),),
            1008: (
                self.equals,
                (param_modes["pos_mode"], param_modes["immediate_mode"]),
            ),
            108: (
                self.equals,
                (param_modes["immediate_mode"], param_modes["pos_mode"]),
            ),
            1108: (
                self.equals,
                (param_modes["immediate_mode"], param_modes["immediate_mode"]),
            ),
            99: (self.terminate, None),
        }
        self.intruction_pointer = 0
        self.intcode_program = intcode_program

    def addition(self, parameter_modes):
        op0 = self.intcode_program[self.intruction_pointer + 1]
        if parameter_modes[0] == 0:
            op0 = self.intcode_program[op0]

        op1 = self.intcode_program[self.intruction_pointer + 2]
        if parameter_modes[1] == 0:
            op1 = self.intcode_program[op1]

        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            op0 + op1
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def mulitplication(self, parameter_modes):
        op0 = self.intcode_program[self.intruction_pointer + 1]
        if parameter_modes[0] == 0:
            op0 = self.intcode_program[op0]

        op1 = self.intcode_program[self.intruction_pointer + 2]
        if parameter_modes[1] == 0:
            op1 = self.intcode_program[op1]

        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            op0 * op1
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def input(self, parameter_modes):
        print("provide integer input: ")
        if parameter_modes[0] == 0:
            self.intcode_program[
                self.intcode_program[self.intruction_pointer + 1]
            ] = int(input())
        else:
            self.intcode_program[self.intruction_pointer + 1] = int(input())

        self.intruction_pointer = self.intruction_pointer + 2
        return True

    def output(self, parameter_modes):
        op0 = self.intcode_program[self.intruction_pointer + 1]
        if parameter_modes[0] == 0:
            op0 = self.intcode_program[op0]
        print(op0)

        self.intruction_pointer = self.intruction_pointer + 2
        return True

    def terminate(self, not_used):
        return False

    def jump_if_true(self, parameter_modes):
        op0 = self.intcode_program[self.intruction_pointer + 1]
        if parameter_modes[0] == 0:
            op0 = self.intcode_program[op0]

        op1 = self.intcode_program[self.intruction_pointer + 2]
        if parameter_modes[1] == 0:
            op1 = self.intcode_program[op1]

        if op0 != 0:
            self.intruction_pointer = op1
        else:
            self.intruction_pointer = self.intruction_pointer + 3
        return True

    def jump_if_false(self, parameter_modes):
        op0 = self.intcode_program[self.intruction_pointer + 1]
        if parameter_modes[0] == 0:
            op0 = self.intcode_program[op0]

        op1 = self.intcode_program[self.intruction_pointer + 2]
        if parameter_modes[1] == 0:
            op1 = self.intcode_program[op1]

        if op0 == 0:
            self.intruction_pointer = op1
        else:
            self.intruction_pointer = self.intruction_pointer + 3
        return True

    def less_than(self, parameter_modes):
        op0 = self.intcode_program[self.intruction_pointer + 1]
        if parameter_modes[0] == 0:
            op0 = self.intcode_program[op0]

        op1 = self.intcode_program[self.intruction_pointer + 2]
        if parameter_modes[1] == 0:
            op1 = self.intcode_program[op1]

        if op0 < op1:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 1
        else:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 0

        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def equals(self, parameter_modes):
        op0 = self.intcode_program[self.intruction_pointer + 1]
        if parameter_modes[0] == 0:
            op0 = self.intcode_program[op0]

        op1 = self.intcode_program[self.intruction_pointer + 2]
        if parameter_modes[1] == 0:
            op1 = self.intcode_program[op1]

        if op0 == op1:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 1
        else:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 0

        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def return_intcode_program(self):
        return self.intcode_program

    def run(self):
        while True:
            handle, params = self.opcodes[self.intcode_program[self.intruction_pointer]]
            if handle(params) == False:
                break
