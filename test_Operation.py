import unittest
from pythonClass.Operation import Operation


class OperationTest(unittest.TestCase):

    def setUp(self):
        self.inputArrayForAdd = [1, 4, 5, 4, 5, 6]
        self.resultArrayAddition = [1, 4, 5, 4, 11, 6]
        self.inputArrayForMultiply = [2, 4, 5, 4, 5, 6]
        self.resultArrayMultiply = [2, 4, 5, 4, 30, 6]
        self.inputArrayForHalt = [99, 4, 5, 4, 5, 6]
        self.resultArrayHalt = [99, 4, 5, 4, 5, 6]
        self.input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        self.output = [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_add_element_first_second_position(self):
        input_array = self.inputArrayForAdd
        op = Operation(input_array)
        result_array = self.resultArrayAddition
        self.assertEqual(result_array, op.compute(input_array))

    def test_should_add_elements_and_return_array_if_first_element_is_1(self):
        input_array = self.inputArrayForAdd
        op = Operation(input_array)
        result_array = self.resultArrayAddition
        self.assertEqual(result_array, op.compute(input_array))

    def test_should_multiply_elements_and_return_array_if_first_element_is_2(self):
        input_array = self.inputArrayForMultiply
        op = Operation(input_array)
        result_array = self.resultArrayMultiply
        self.assertEqual(result_array, op.compute(input_array))

    def test_should_halt_operation__if_first_element_is_99(self):
        input_array = self.inputArrayForMultiply
        op = Operation(input_array)
        result_array = self.resultArrayMultiply
        self.assertEqual(result_array, op.compute(input_array))

    def test_new(self):
        input_array = self.input
        op = Operation(input_array)
        result_array = self.output
        self.assertEqual(result_array, op.compute(input_array))


if __name__ == '__main__':
    unittest.main()
