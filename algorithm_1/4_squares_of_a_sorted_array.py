import unittest
from typing import *

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        answer = [0] * len(nums)
        idx = len(nums) - 1
        while l <= r:
            l_v, r_v = nums[l], nums[r]
            if abs(l_v) > abs(r_v):
                answer[idx] = l_v ** 2
                l += 1
            else:
                answer[idx] = r_v ** 2
                r -= 1
            idx -= 1
        return answer

                

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
       nums = [-4,-1,0,3,10]
       answer = [0,1,9,16,100]
       result = self.sol.sortedSquares(nums)
       self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()