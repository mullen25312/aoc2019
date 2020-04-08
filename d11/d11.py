from utils.intcode_computer import IntcodeComputer
from collections import defaultdict


class PaintRobot:
    def __init__(self, programm):
        self.cpu = IntcodeComputer(programm)
        self.posx = 0
        self.posy = 0
        self.orientation = 0
        self.canvas = defaultdict(int, {})

    def paint(self):
        # run paint robot until program is terminated
        while not self.cpu.terminated():
            # provide current color as input and run first time
            self.cpu.inputs.append(self.canvas[(self.posx, self.posy)])
            self.cpu.run()

            # color canvas and run second time
            self.canvas[(self.posx, self.posy)] = self.cpu.outputs[-1]
            self.cpu.run()

            # rotate and move according to output
            self.rotate()
            self.move()

    def rotate(self):
        if self.cpu.outputs[-1] == 0:
            self.orientation = (self.orientation - 1) % 4
        else:
            self.orientation = (self.orientation + 1) % 4

    def move(self):
        if self.orientation % 2 != 0:
            self.posx += 1 if self.orientation == 1 else -1
        else:
            self.posy += 1 if self.orientation == 2 else -1

    def show_canvas(self):
        # get maximum coordinates assuming robot stays in first quadrant
        # xmin = min(self.canvas.keys(), key=lambda item: item[0])[0]
        xmax = max(self.canvas.keys(), key=lambda item: item[0])[0]
        # ymin = min(self.canvas.keys(), key=lambda item: item[1])[1]
        ymax = max(self.canvas.keys(), key=lambda item: item[1])[1]

        # render output string
        output_str = [[*[" " for _ in range(xmax + 1)], "\n"] for _ in range(ymax + 1)]
        for pos in self.canvas:
            output_str[pos[1]][pos[0]] = "#" if self.canvas[pos] == 1 else " "
        output_str = [char for line in output_str for char in line]

        # return output string
        return "".join(output_str)


class DailyPuzzle11:
    def __init__(self):
        self.data = None

    def read_data(self):
        # read input data
        with open("./d11/input.txt") as f:
            lines = f.readline().split(",")
            self.data = [int(line) for line in lines]

    def solve_part_one(self):
        paint_robot = PaintRobot(self.data.copy())
        paint_robot.paint()
        return len(paint_robot.canvas)
        # return paint_robot.show_canvas()

    def solve_part_two(self):
        paint_robot = PaintRobot(self.data.copy())
        paint_robot.canvas[(0, 0)] = 1
        paint_robot.paint()
        return paint_robot.show_canvas()
