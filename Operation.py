class Operation:

    def __init__(self, arr):
        self.arr = arr

    def compute(self, position):
        pos = 0

        start = position[pos]

        a, b, result = self.parameters(pos, position)

        if start == 1:
            addition = a + b
            position[result] = addition
            return position

        if start == 2:
            multiply = a * b
            position[result] = multiply
            return position

        return position

    def parameters(self, pos, position):
        first = position[pos + 1]
        second = position[pos + 2]
        result = pos + 3
        a = position[first]
        b = position[second]
        return a, b, result
