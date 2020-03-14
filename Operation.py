class Operation:

    def __init__(self, arr):
        self.arr = arr

    def compute(self, position):
        pos = 0

        start = position[pos]

        if start == 1:
            first = pos + 1
            second = pos + 2
            result = pos + 3

            a = position[first]
            b = position[second]

            addition = a + b
            position[result] = addition

            return position
