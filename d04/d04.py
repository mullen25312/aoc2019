def numberOfValidCodes(digit, decimalPower):
    if decimalPower == 0:
        return 1
    else:
        if digit == 0: return sum(numberOfValidCodes(range(0,11), decimalPower-1))
        else: return numberOfValidCodes(digit-1, decimalPower) - numberOfValidCodes(digit-1, decimalPower-1)


class d04:
    def __init__(self):
        self.number1 = []
        self.number2 = []


    def readData(self):
        self.number1 = 284639
        self.number2 = 748759


    def solvePartOne(self):
        return numberOfValidCodes(2,1)


    def solvePartTwo(self):
        return True


    