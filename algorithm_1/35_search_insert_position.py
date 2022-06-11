from unittest import TestCase
import unittest
from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        target 이 nums 에 존재하면 index 를, 없다면 insert 해야 할 위치를 return 

        어떤 값을 return 해야 할 지 고민된다면, 루프가 종료되기 직전의 상황을 보고 판단하면 된다.
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
        
        return l

class SolutionTest(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_exmaples(self):
        tc = [
            ([1,3,5,6], 5, 2),
            ([1,3,5,6], 2, 1),
            ([1,3,5,6], 7, 4)
        ]

        for idx, tc in enumerate(tc):
            with self.subTest(idx=idx):
                answer = self.sol.searchInsert(tc[0], tc[1])
                self.assertEqual(tc[2], answer)

if __name__ == '__main__':
    unittest.main()