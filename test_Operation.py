import unittest
from pythonClass.Operation import Operation


class OperationTest(unittest.TestCase):

    def setUp(self):
        self.addInputArrayOne = [1, 4, 5, 4, 5, 6]
        self.resultArrayOne = [1, 4, 5, 11, 5, 6]

    def test_add(self):
        input_array = self.addInputArrayOne
        op = Operation(input_array)
        result_array = self.resultArrayOne
        self.assertEqual(result_array, op.compute(input_array))

    def test_should_add_elements_and_return_array(self):
        input_array = self.addInputArrayOne
        op = Operation(input_array)
        result_array = self.resultArrayOne
        self.assertEqual(result_array, op.compute(input_array))



if __name__ == '__main__':
    unittest.main()
