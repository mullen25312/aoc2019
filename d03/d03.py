
class d03:
    def __init__(self):
        self.line1 = []
        self.line2 = []


    def readData(self):
        print('data read')
        with open('./d03/input.txt') as f:
            self.line1 = f.readline().split(",")
            self.line2 = f.readline().split(",")
            #self.line1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(",")
            #self.line2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(",")


    def solvePartOne(self):
        # create list of positions of line1
        line1Positions = set()
        pos = [0,0]
        for move in enumerate(self.line1):
            direction = move[1][0]
            distance = int(move[1][1:])

            if direction == 'R': # moved to the right
                for step in range(1,distance+1):
                    line1Positions.add((pos[0] + step, pos[1]))
                pos[0] += distance

            if direction == 'L': # moved to the left
                for step in range(1,distance+1):
                    line1Positions.add((pos[0] - step, pos[1]))
                pos[0] -= distance

            if direction == 'U': # moved up
                for step in range(1,distance+1):
                    line1Positions.add((pos[0], pos[1] + step))
                pos[1] += distance

            if direction == 'D': # moved down
                for step in range(1,distance+1):
                    line1Positions.add((pos[0], pos[1] - step))
                pos[1] -= distance

        # create list of positions of line2
        line2Positions = set()
        pos = [0,0]
        for move in enumerate(self.line2):
            direction = move[1][0]
            distance = int(move[1][1:])

            if direction == 'R': # moved to the right
                for step in range(1,distance+1):
                    line2Positions.add((pos[0] + step, pos[1]))
                pos[0] += distance

            if direction == 'L': # moved to the left
                for step in range(1,distance+1):
                    line2Positions.add((pos[0] - step, pos[1]))
                pos[0] -= distance

            if direction == 'U': # moved up
                for step in range(1,distance+1):
                    line2Positions.add((pos[0], pos[1] + step))
                pos[1] += distance

            if direction == 'D': # moved down
                for step in range(1,distance+1):
                    line2Positions.add((pos[0], pos[1] - step))
                pos[1] -= distance

        crossings = line1Positions.intersection(line2Positions)
        distances = [abs(point[0]) + abs(point[1]) for point in list(crossings)]
        return  min(distances)

    def solvePartTwo(self):
        return True


    