import sys


class Operation:

    def compute(self, puzzle):

        pos = 0

        while pos <= len(puzzle) - 4:

            start = puzzle[pos]

            a, b, result = self.parameters(pos, puzzle)
            output = puzzle[result]

            if start == 1:
                output = self.addvalue(a, b)

            if start == 2:
                output = self.multiplyvalue(a, b)

            if start == 99:
                return puzzle

            puzzle[result] = output
            pos += 4

        return puzzle

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
