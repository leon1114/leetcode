import unittest
from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        0 을 뒤쪽으로 옮기는데 0 이 아닌 것들은 순서가 유지 되어야 한다.

        0, 1, 0, 3, 12 -> 1, 3, 12, 0, 0

        0 idx, non zero index 를 유지한다. 
        >> 0 idx = 가장 앞쪽에 남아있는 0 
        >> non zero idx = 0 idx 보다 뒤쪽에 있는 non zero num 중 가장 앞쪽에 있는 숫자 

        non zero idx 가 len(nums) 까지 옮겨지면 끝남. 

        0 1 0 3 12 -> zi: 0, nzi: 1 -> swap -> 1 0 0 3 12 
        1 0 0 3 12 -> zi: 1, nzi: 3 -> swap -> 1 3 0 0 12
        1 3 0 0 12 -> zi: 2, nzi: 4 -> swap -> 1 3 12 0 0
        1 3 12 0 0 -> zi: 3, nzi: 5 -> end

        """
        zi, nzi = 0, 0

        while True:
            while zi < len(nums) and nums[zi] != 0:
                zi += 1

            nzi = zi
            while nzi < len(nums) and nums[nzi] == 0:
                nzi += 1

            if zi >= len(nums) or nzi >= len(nums):
                break
            
            nums[zi], nums[nzi] = nums[nzi], nums[zi]


class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tests(self):
        tc = [
            ([0,1,0,3,12], [1,3,12,0,0]),
            ([0], [0])
        ]

        for idx, _tc in enumerate(tc):
            with self.subTest(idx=idx):
                self.sol.moveZeroes(_tc[0])
                self.assertEqual(_tc[0], _tc[1])


if __name__ == "__main__":
    unittest.main()