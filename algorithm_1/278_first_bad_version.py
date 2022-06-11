from unittest import TestCase
import unittest
from typing import *

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

BAD_VERSION = None
def isBadVersion(version: int) -> bool:
    if version >= BAD_VERSION:
        return True
    else:
        return False


class Solution:
    """
    처음에는 bad_version = m 과 같이 세팅해놓고 return bad_version 했음. 

    그런데 그냥 l 을 반환해도 됨. 왜? 
    >> 종료 조건을 생각해보면 됨. 
       
       결국 l 과 r 이 만났다면, 그 위치가 가장 첫 에러 버전임. 
       여기서는 r 이 l 보다 작아지면서 루프가 종료됨. 즉 l 에 정답 위치가 남아있게 됨. 
    """
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n # r inclusive
        
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1

        return l


class SolutionTest(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_exmaple_1(self):
        global BAD_VERSION
        n = 5
        BAD_VERSION = 4
        self.assertEqual(self.sol.firstBadVersion(n), BAD_VERSION)

    def test_exmaple_1(self):
        global BAD_VERSION
        n = 1
        BAD_VERSION = 1
        self.assertEqual(self.sol.firstBadVersion(n), BAD_VERSION)

if __name__ == '__main__':
    unittest.main()