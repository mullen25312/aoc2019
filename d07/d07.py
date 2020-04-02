import math

from utils.intcode_computer import IntcodeComputer
from itertools import permutations


class DailyPuzzle07:
    def __init__(self):
        self.data = None

    def read_data(self):
        with open("./d07/input.txt") as f:
            lines = f.readline().split(",")
            self.data = [int(line) for line in lines]

    def solve_part_one(self):
        program = self.data.copy()

        # initialize loop over all permutations of valid phase settings
        thruster_signals = []
        phase_setting_permutations = list(permutations(range(0, 5)))

        # loop over all permutations of valid phase settings
        for phase_settings in phase_setting_permutations:
            # initialize first amplifier (with input zero)
            amps = []
            amps.append(IntcodeComputer(program, [phase_settings[0], 0]))
            amps[0].run()

            # run all other amplifier (with input as output of the one before)
            for phase in phase_settings[1:]:
                amps.append(IntcodeComputer(program, [phase, amps[-1].outputs[0]]))
                amps[-1].run()

            # save thruster output for this permutation of valid phase settings
            thruster_signals.append(amps[-1].outputs[0])

        # return maximum thruster output
        return max(thruster_signals)

    def solve_part_two(self):
        program = self.data.copy()

        # initialize loop over all permutations of valid phase settings
        thruster_signals = []
        phase_setting_permutations = list(permutations(range(5, 10)))

        ## loop over all permutations of valid phase settings
        for phase_settings in phase_setting_permutations:
            amps = []
            amps.append(IntcodeComputer(program, [phase_settings[0], 0]))
            amps[0].run()

            # first feed forward
            for phase in phase_settings[1:]:
                amps.append(IntcodeComputer(program, [phase, amps[-1].outputs[0]]))
                amps[-1].run()

            # run feddback until one of the amplifiers terminates
            while not any([amp.terminated() for amp in amps]):
                for idx, phase in enumerate(phase_settings):
                    amps[idx].inputs.append(amps[idx - 1].outputs[-1])
                    amps[idx].run()

            # save thruster output for this permutation of valid phase settings
            thruster_signals.append(amps[-1].outputs[-1])

        # return maximum thruster output
        return max(thruster_signals)
