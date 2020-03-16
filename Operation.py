import sys


class Operation:

    def __init__(self, arr):
        self.arr = arr

    def compute(self, position):

        pos = 0

        while pos < len(position)-4:

            start = position[pos]

            a, b, result = self.parameters(pos, position)
            output = position[result]

            if start == 1:
                output = self.addvalue(a, b)

            if start == 2:
                output = self.multiplyvalue(a, b)

            if start == 99:
                sys.exit()

            position[result] = output
            pos += 4

        return position

    def addvalue(self, a, b):
        return a + b


    def multiplyvalue(self, a, b):
        return a * b


    def parameters(self, pos, position):
        first = position[pos + 1]
        second = position[pos + 2]
        result = position[pos + 3]
        a = position[first]
        b = position[second]
        return a, b, result
