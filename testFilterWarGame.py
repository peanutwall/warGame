import os
import sys

DIRNAME = os.path.dirname(__file__)
sys.path.append(os.path.join(DIRNAME))
import unittest
from ddt import ddt, data, unpack
import numpy as np
from filterWarGame import *

@ddt
class TestFilterFunctions(unittest.TestCase):
    def setUp(self):
        self.testParameter = 0


    @data(([4, 4, 4], [0, 0, 0], [0, 0, 0], [0, 0, 0], [[3, 2, 1], [0, 0, 0]]),
          ([0, 0, 0], [4, 4, 4], [0, 0, 0], [0, 0, 0], [[0, 0, 0], [1, 2, 3]]),
          ([10, 10, 10], [15, 15, 15], [10, 10, 10], [0, 0, 0], [[3, 2, 1], [0, 0, 0]]))
    @unpack
    def testCalculateRemainingSoldiers(self, policyA, policyB, remainingSoldiersA, remainingSoldiersB, groundTruth):
        result = calculateRemainingSoldiers(policyA, policyB, remainingSoldiersA, remainingSoldiersB)
        truthValue = np.array_equal(result, groundTruth)
        self.assertTrue(truthValue)

    @data(([1, 1, 1], [34, 20]),
          ([2, 2, 2], [20, 34]),
          ([1, 2, 2], [27, 32]),
          ([0, 0, 0], [20, 20]))

    @unpack
    def testCalculateSoldiers(self, warField, groundTruth):
        result = calculateSoldiers(warField)
        truthValue = np.array_equal(result, groundTruth)
        self.assertTrue(truthValue)

if __name__ == '__main__':
    unittest.main()








