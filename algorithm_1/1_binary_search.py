from unittest import TestCase
import unittest
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order, 
        and an integer target, write a function to search target in nums. 
        If target exists, then return its index. Otherwise, return -1.
        """

        l, r = 0, len(nums) # r exclusive 

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            else:
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1    

        return -1


class SolutionTest(TestCase):

    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    
    def test_example_1(self):
        nums = [-1,0,3,5,9,12]
        target = 9
        result = self.sol.search(nums, target)
        self.assertEqual(4, result)

    def test_example_1(self):
        nums = [-1,0,3,5,9,12]
        target = 2
        result = self.sol.search(nums, target)
        self.assertEqual(-1, result)
    

if __name__ == '__main__':
    unittest.main()