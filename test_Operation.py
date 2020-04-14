import unittest
from pythonClass.Operation import Operation


class OperationTest(unittest.TestCase):

    def setUp(self):
        self.input = [1, 2, 3, 3]
        self.output = [1, 2, 3, 6]
        self.inputOne = [1, 0, 0, 0, 99]
        self.outputOne = [2, 0, 0, 0, 99]
        self.inputTwo = [2, 3, 0, 3, 99]
        self.outputTwo = [2, 3, 0, 6, 99]
        self.inputThree = [2, 4, 4, 5, 99, 0]
        self.outputThree = [2, 4, 4, 5, 99, 9801]
        self.inputFour = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        self.outputFour = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.puzzle_input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 6, 27,
                             1, 9, 27, 31, 1, 31, 10, 35, 2, 13, 35, 39, 1, 39, 10, 43, 1, 43, 9, 47, 1, 47, 13, 51, 1,
                             51, 13, 55, 2, 55, 6, 59, 1, 59, 5, 63, 2, 10, 63, 67, 1, 67, 9, 71, 1, 71, 13, 75, 1, 6,
                             75, 79, 1, 10, 79, 83, 2, 9, 83, 87, 1, 87, 5, 91, 2, 91, 9, 95, 1, 6, 95, 99, 1, 99, 5,
                             103, 2, 103, 10, 107, 1, 107, 6, 111, 2, 9, 111, 115, 2, 9, 115, 119, 2, 13, 119, 123, 1,
                             123, 9, 127, 1, 5, 127, 131, 1, 131, 2, 135, 1, 135, 6, 0, 99, 2, 0, 14, 0]

    def test_should_halt_operation__if_first_element_is_99(self):
        input_array = self.input
        op = Operation()
        result_array = self.output
        self.assertEqual(result_array, op.compute(input_array))

    def test_add_element_if_start_is_1(self):
        input_array = self.inputOne
        op = Operation()
        result_array = self.outputOne
        self.assertEqual(result_array, op.compute(input_array))

    def test_multiply_element_if_start_is_1(self):
        input_array = self.inputTwo
        op = Operation()
        result_array = self.outputTwo
        self.assertEqual(result_array, op.compute(input_array))

    def test_multiply_elements_and_store_result_in_specified_index(self):
        input_array = self.inputThree
        op = Operation()
        result_array = self.outputThree
        self.assertEqual(result_array, op.compute(input_array))

    def test_add_multiply_elements_and_store_result_in_specified_index(self):
        input_array = self.inputFour
        op = Operation()
        result_array = self.outputFour
        self.assertEqual(result_array, op.compute(input_array))


if __name__ == '__main__':
    unittest.main()
