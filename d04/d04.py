def get_digits(number):
    digits = []
    while number != 0:
        digits.append(number % 10)
        number = number // 10
    digits.reverse()
    return digits


def criteria_one(number):
    digit = number % 10
    number = number // 10
    while number != 0:
        tmp = number % 10
        if tmp == digit:
            return True
        number = number // 10
        digit = tmp
    return False


def criteria_two(number):
    digit = number % 10
    number = number // 10
    while number != 0:
        tmp = number % 10
        if tmp > digit:
            return False
        number = number // 10
        digit = tmp
    return True


def criteria_three(number):
    digits = get_digits(number)
    idx = 0
    while idx < len(digits):
        idx2 = 0
        while digits[idx] == digits[idx + idx2]:
            idx2 = idx2 + 1
            if idx + idx2 > len(digits) - 1:
                idx = len(digits) - 1
                break
        idx = idx + idx2
        if idx2 == 2:
            return True
    return False


class DailyPuzzle:
    def __init__(self):
        self.number1 = []
        self.number2 = []

    def read_data(self):
        self.number1 = 284639
        self.number2 = 748759

    def solve_part_one(self):
        cnt = 0
        for number in range(self.number1, self.number2):
            if criteria_one(number) and criteria_two(number):
                cnt = cnt + 1
        return cnt

    def solve_part_two(self):
        cnt = 0
        for number in range(self.number1, self.number2):
            if criteria_one(number) and criteria_two(number) and criteria_three(number):
                cnt = cnt + 1
        return cnt
