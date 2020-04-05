def render_picture(pic, width):
    pic_for_display = []
    for idx in range(len(pic)):
        pic_for_display.append("\u2588" if pic[idx] else " ")
        pic_for_display.append("\n" if (idx + 1) % width == 0 else "")
    return "".join(pic_for_display)


class DailyPuzzle08:
    def __init__(self):
        self.data = None
        self.width = 0
        self.height = 0

    def read_data(self):
        # read input data
        with open("./d08/input.txt") as f:
            digits = list(f.readline()[:-1])
            raw_data = [int(digit) for digit in digits]

        # specify pcitrue/layer width and height
        self.width = 25
        self.height = 6

        # split raw data into list of layers (lists of integer themselves)
        self.data = []
        layer_size = self.width * self.height
        for layer in range(0, round(len(raw_data) / layer_size)):
            self.data.append(raw_data[layer * layer_size : (layer + 1) * layer_size])

    def solve_part_one(self):
        # determine sum of zeros for each layer
        sum_of_zeros = [sum([pixel == 0 for pixel in layer]) for layer in self.data]

        # determine layer with fewest some of zero
        fewest_zero_layer = self.data[sum_of_zeros.index(min(sum_of_zeros))]

        # detmine number of ones and twos within this layer
        number_of_ones = sum([pixel == 1 for pixel in fewest_zero_layer])
        number_of_twos = sum([pixel == 2 for pixel in fewest_zero_layer])

        # return their product
        return number_of_ones * number_of_twos

    def solve_part_two(self):
        # initilize picture result
        pic = self.data[0]  # [2 for pixel in self.data[0]]

        # for every pixel determine color by going through layer top to down (break if non-transparent)
        for idx in range(len(pic)):
            for layer in self.data:
                if layer[idx] != 2:
                    pic[idx] = layer[idx]
                    break

        # return console rendered picture
        return render_picture(pic, self.width)
