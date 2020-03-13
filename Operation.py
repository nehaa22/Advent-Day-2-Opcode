class Operation:

    def __init__(self, arr):
        self.arr = arr

    def compute(self, arr):
        index = 0
        if arr[index] == 1:
            arr[index + 3] = arr[index + 1] + arr[index + 2]
            return arr[index+3]
