import unittest
import numpy as np
from pythonClass.Operation import Operation


class OperationTest(unittest.TestCase):

    def setUp(self):
        self.addInputArrayOne = [1, 3, 3, 4]
        self.resultArrayOne = [1, 3, 3, 6]

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
