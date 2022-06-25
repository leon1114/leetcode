from typing import *
import unittest

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        pass


class SolutionTest(unittest.TestCase):
    def test_example(self):
        sol = Solution()
        nums = [1,2,3]
        multipliers = [3,2,1]
        answer = 14
        self.assertEqual(sol.maximumScore(nums, multipliers), answer)


    def test_example_2(self):
        sol = Solution()
        nums = [-5,-3,-3,-2,7,1]
        multipliers = [-10,-5,3,4,6]
        answer = 102
        self.assertEqual(sol.maximumScore(nums, multipliers), answer)


if __name__ == '__main__':
    unittest.main()