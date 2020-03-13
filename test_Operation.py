import unittest
import numpy as np
from pythonClass.Operation import Operation


class OperationTest(unittest.TestCase):

    def setUp(self):
        self.addInputArrayOne = [1, 3, 3, 4]

    def test_add(self):
        addarray = np.array(self.addInputArrayOne)
        op = Operation(addarray)
        self.assertEqual(6, op.compute(addarray))


if __name__ == '__main__':
    unittest.main()
