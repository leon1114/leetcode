import unittest
from typing import *

# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        cookies list 에 있는 element 들을 k 개로 bagging 하는데, 들어있는 값들의 합이 최대인 bag 가 최소의 합을 갖도록 해야 함. 
        back tracking?
        """
        pass


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        cookies = [8,15,10,20,8]
        k = 2
        result = self.sol.distributeCookies(cookies, k)
        answer = 31
        self.assertEqual(answer, result)

    def test_example_2(self):
        cookies = [6,1,3,2,2,4,1,2]
        k = 3
        result = self.sol.distributeCookies(cookies, k)
        answer = 7
        self.assertEqual(answer, result)
        

if __name__ == '__main__':
    unittest.main()