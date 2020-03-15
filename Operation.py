class Operation:

    def __init__(self, arr):
        self.arr = arr

    def compute(self, position):
        pos = 0

        start = position[pos]

        a, b, result = self.parameters(pos, position)
        output = position[result]

        if start == 1:
            output = a + b

        if start == 2:
            output = a * b

        position[result] = output
        return position

    def parameters(self, pos, position):
        first = position[pos + 1]
        second = position[pos + 2]
        result = pos + 3
        a = position[first]
        b = position[second]
        return a, b, result
