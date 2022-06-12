import unittest
from typing import *

# https://leetcode.com/contest/weekly-contest-297/problems/calculate-amount-paid-in-taxes/

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total = 0
        lower = 0
        for i in range(len(brackets)):
            upper = brackets[i][0] if income > brackets[i][0] else income
            total += (upper - lower) * brackets[i][1] / 100
            lower = upper
        
        return total


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        brackets = [[3,50],[7,10],[12,25]]
        income = 10
        answer = 2.65000
        result = self.sol.calculateTax(brackets, income)
        self.assertEqual(answer, result)

    def test_example_2(self):
        brackets = [[1,0],[4,25],[5,50]]
        income = 2
        answer = 0.25000
        result = self.sol.calculateTax(brackets, income)
        self.assertEqual(answer, result)
    
    def test_example_3(self):
        brackets = [[2,50]]
        income = 0
        answer = 0.0
        result = self.sol.calculateTax(brackets, income)
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()