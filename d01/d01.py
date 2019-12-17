import math

class d01:
    def __init__(self):
        self.data = []


    def readData(self):
        with open('./d01/input.txt') as f:
            tmp= f.readlines()
            self.data = [int(i) for i in tmp]


    def solvePartOne(self):
        return sum([max((math.floor(value / 3) - 2,0)) for value in self.data])
    
    
    def solvePartTwo(self):
        data = [max((math.floor(value / 3) - 2,0)) for value in self.data]
        result = data
        while any(value != 0 for value in data):
            data = [max((math.floor(value / 3) - 2,0)) for value in data]
            result = result + data
        return sum(result)

    