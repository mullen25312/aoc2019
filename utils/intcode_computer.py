p_modes = {"position": 0, "immediate": 1}


class IntcodeComputer:
    def __init__(self, intcode_program, inputs=[]):
        self.opcodes = {
            # addition
            1: (self.addition, (p_modes["position"], p_modes["position"])),
            1001: (self.addition, (p_modes["position"], p_modes["immediate"])),
            101: (self.addition, (p_modes["immediate"], p_modes["position"])),
            1101: (self.addition, (p_modes["immediate"], p_modes["immediate"])),
            # muliplication
            2: (self.mulitplication, (p_modes["position"], p_modes["position"])),
            1002: (self.mulitplication, (p_modes["position"], p_modes["immediate"])),
            102: (self.mulitplication, (p_modes["immediate"], p_modes["position"])),
            1102: (self.mulitplication, (p_modes["immediate"], p_modes["immediate"])),
            # input
            3: (self.input, (p_modes["position"],)),
            103: (self.input, (p_modes["immediate"],)),
            # output
            4: (self.output, (p_modes["position"],)),
            104: (self.output, (p_modes["immediate"],)),
            # jump if true
            5: (self.jump_if_true, (p_modes["position"], p_modes["position"])),
            1005: (self.jump_if_true, (p_modes["position"], p_modes["immediate"])),
            105: (self.jump_if_true, (p_modes["immediate"], p_modes["position"])),
            1105: (self.jump_if_true, (p_modes["immediate"], p_modes["immediate"])),
            # jumo if false
            6: (self.jump_if_false, (p_modes["position"], p_modes["position"])),
            1006: (self.jump_if_false, (p_modes["position"], p_modes["immediate"])),
            106: (self.jump_if_false, (p_modes["immediate"], p_modes["position"])),
            1106: (self.jump_if_false, (p_modes["immediate"], p_modes["immediate"])),
            # less than
            7: (self.less_than, (p_modes["position"], p_modes["position"])),
            1007: (self.less_than, (p_modes["position"], p_modes["immediate"])),
            107: (self.less_than, (p_modes["immediate"], p_modes["position"])),
            1107: (self.less_than, (p_modes["immediate"], p_modes["immediate"])),
            # equals
            8: (self.equals, (p_modes["position"], p_modes["position"])),
            1008: (self.equals, (p_modes["position"], p_modes["immediate"])),
            108: (self.equals, (p_modes["immediate"], p_modes["position"])),
            1108: (self.equals, (p_modes["immediate"], p_modes["immediate"])),
            99: (self.terminate, None),
        }
        self.intruction_pointer = 0
        self.intcode_program = intcode_program
        self.inputs = inputs
        self.outputs = []

    def parse_parameter(self, parameter_modes):
        args = list(parameter_modes)
        for idx, param_mode in enumerate(parameter_modes):
            args[idx] = self.intcode_program[self.intruction_pointer + idx + 1]
            if param_mode == p_modes["position"]:
                args[idx] = self.intcode_program[args[idx]]
        return args

    def addition(self, parameter_modes):
        args = self.parse_parameter(parameter_modes)

        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            args[0] + args[1]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def mulitplication(self, parameter_modes):
        args = self.parse_parameter(parameter_modes)

        self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = (
            args[0] * args[1]
        )
        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def input(self, parameter_modes):
        if parameter_modes[0] == 0:
            self.intcode_program[
                self.intcode_program[self.intruction_pointer + 1]
            ] = self.inputs[0]
        else:
            self.intcode_program[self.intruction_pointer + 1] = self.inputs[0]

        self.intruction_pointer = self.intruction_pointer + 2
        self.inputs.pop(0)
        return True

    def output(self, parameter_modes):
        args = self.parse_parameter(parameter_modes)
        self.outputs.append(args[0])

        self.intruction_pointer = self.intruction_pointer + 2
        return False

    def jump_if_true(self, parameter_modes):
        args = self.parse_parameter(parameter_modes)

        if args[0] != 0:
            self.intruction_pointer = args[1]
        else:
            self.intruction_pointer = self.intruction_pointer + 3
        return True

    def jump_if_false(self, parameter_modes):
        args = self.parse_parameter(parameter_modes)

        if args[0] == 0:
            self.intruction_pointer = args[1]
        else:
            self.intruction_pointer = self.intruction_pointer + 3
        return True

    def less_than(self, parameter_modes):
        args = self.parse_parameter(parameter_modes)

        if args[0] < args[1]:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 1
        else:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 0

        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def equals(self, parameter_modes):
        args = self.parse_parameter(parameter_modes)

        if args[0] == args[1]:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 1
        else:
            self.intcode_program[self.intcode_program[self.intruction_pointer + 3]] = 0

        self.intruction_pointer = self.intruction_pointer + 4
        return True

    def terminate(self, not_used):
        return False

    def run(self):
        while True:
            handle, params = self.opcodes[self.intcode_program[self.intruction_pointer]]
            if handle(params) == False:
                break

    def run_until_termination(self):
        while True:
            handle, params = self.opcodes[self.intcode_program[self.intruction_pointer]]
            if handle(params) == False and handle == self.terminate:
                break

    def terminated(self):
        return self.intcode_program[self.intruction_pointer] == 99
