import unittest
from pythonClass.Operation import Operation


class OperationTest(unittest.TestCase):

    def setUp(self):
        self.input = [1, 2, 3, 4, 88, 88]
        self.output = [1, 2, 3, 4, 7, 88]
        self.inputOne = [1, 0, 0, 0, 99]
        self.outputOne = [2, 0, 0, 0, 99]
        self.inputTwo = [2, 3, 0, 3, 99]
        self.outputTwo = [2, 3, 0, 6, 99]
        self.inputThree = [2, 4, 4, 5, 99, 0]
        self.outputThree = [2, 4, 4, 5, 99, 9801]
        self.inputFour = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        self.outputFour = [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_should_halt_operation__if_first_element_is_99(self):
        input_array = self.input
        op = Operation(input_array)
        result_array = self.output
        self.assertEqual(result_array, op.compute(input_array))

    def test_add_element_if_start_is_1(self):
        input_array = self.inputOne
        op = Operation(input_array)
        result_array = self.outputOne
        self.assertEqual(result_array, op.compute(input_array))

    def test_should_add_elements_and_return_array_if_first_element_is_1(self):
        input_array = self.inputTwo
        op = Operation(input_array)
        result_array = self.outputTwo
        self.assertEqual(result_array, op.compute(input_array))

    def test_should_multiply_elements_and_return_array_if_first_element_is_2(self):
        input_array = self.inputThree
        op = Operation(input_array)
        result_array = self.outputThree
        self.assertEqual(result_array, op.compute(input_array))

    def test_new(self):
        input_array = self.inputFour
        op = Operation(input_array)
        result_array = self.outputFour
        self.assertEqual(result_array, op.compute(input_array))


if __name__ == '__main__':
    unittest.main()
