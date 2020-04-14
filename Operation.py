class Operation:

    # todo - long function
    # todo - unused arguments, nounvalue and verbvalue
    # todo - arguemnets not in python syntax - snake case. we have no case. e.g. noun_value
    def compute(self, puzzle):

        index = 0

        # todo - long loop
        while index <= len(puzzle) - 4:  # todo - magic number 4.

            opcode = puzzle[index]

            a, b, result = self.parameters(index, puzzle)  # todo - what's a and b?
            value = puzzle[result]
            # todo - magic nu,mber 1. what is that?
            if opcode == 1:  # todo - hardcoded conditions, no polymorphism used.
                value = self.addvalue(a, b)  # todo - python naming

            # todo - magic number 2. what is that?
            if opcode == 2:
                value = self.multiplyvalue(a, b)

            # todo - magic number 99. what is that?
            if opcode == 99:
                return puzzle

            puzzle[result] = value
            index += 4  # todo - again 4. oh we are updating the counter. why did we not use for loop then?

        return puzzle  # todo - why is the output maintained in the first element of array? maybe it can be tter

    # todo - in its current state these 2 methods offer no advantage.
    # todo - why not just use "+" ?? in line 23?
    def addvalue(self, a, b):
        return a + b

    def multiplyvalue(self, a, b):
        return a * b

    def parameters(self, pos, position):  # todo - function name does not explain what it is at all
        first = position[pos + 1]
        second = position[pos + 2]
        result = position[pos + 3]
        a = position[first]
        b = position[second]
        return a, b, result


puzzle_input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 6, 27,
                1, 9, 27, 31, 10, 35, 2, 13, 35, 39, 1, 39, 10, 43, 1, 43, 9, 47, 1, 47, 13, 51, 1,
                51, 13, 55, 2, 55, 6, 59, 1, 59, 5, 63, 2, 10, 63, 67, 1, 67, 9, 71, 1, 71, 13, 75, 1, 6,
                75, 79, 1, 10, 79, 83, 2, 9, 83, 87, 1, 87, 5, 91, 2, 91, 9, 95, 1, 6, 95, 99, 1, 99, 5,
                103, 2, 103, 10, 107, 1, 107, 6, 111, 2, 9, 111, 115, 2, 9, 115, 119, 2, 13, 119, 123, 1,
                123, 9, 127, 1, 5, 127, 131, 1, 131, 2, 135, 1, 135, 6, 0, 99, 2, 0, 14, 0]

call = Operation()

# todo - is this part of test or code? Makes no sense...
target = 19690720
for noun in range(100):
    for verb in range(100):
        output = call.compute(puzzle_input)
        if output == target:
            print(noun, verb, 100 * noun + verb)
            break
