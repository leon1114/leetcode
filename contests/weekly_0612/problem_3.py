import unittest
from typing import *

# https://leetcode.com/problems/fair-distribution-of-cookies/

import math
class Solution:
    """
    Runtime: 90 ms, faster than 100.00% of Python3 online submissions for Fair Distribution of Cookies.
    Memory Usage: 13.9 MB, less than 37.50% of Python3 online submissions for Fair Distribution of Cookies.
    """
    def bt(self, cookie_idx: int):
        """
        cookie_idx 에 해당하는 cookie 를 하나의 bag 에 넣고, 다음 cookie_idx 대상으로 bt 호출


        """
        # 종료조건 설정
        if max(self.bags) >= self.min_max:
            return

        if cookie_idx == len(self.cookies):
            max_value = max(self.bags)
            if max_value < self.min_max:
                self.min_max = max_value
            return 

        # 각 가방 하나씩 순회하면서 쿠키를 넣어봄. 
        for idx in range(len(self.bags)):
            self.bags[idx] += self.cookies[cookie_idx]
            self.bt(cookie_idx+1)
            self.bags[idx] -= self.cookies[cookie_idx]


    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        cookies list 에 있는 element 들을 k 개로 bagging 하는데, 들어있는 값들의 합이 최대인 bag 가 최소의 합을 갖도록 해야 함. 
        back tracking?
        """

        self.bags = [0] * k
        self.cookies = cookies
        self.min_max = math.inf
        self.bt(0)
        return self.min_max


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