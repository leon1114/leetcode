import unittest
from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

                

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        answer = [5,6,7,1,2,3,4]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, answer)

    def test_example_2(self):
        nums = [1,2]
        k = 5
        answer = [2,1]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, answer)

if __name__ == '__main__':
    unittest.main()