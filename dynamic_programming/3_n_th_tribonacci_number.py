from typing import *

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1

        n_3, n_2, n_1 = 0, 1, 1

        for i in range(3, n+1):
            ans = n_3 + n_2 + n_1
            n_3, n_2, n_1 = n_2, n_1, ans
        
        return ans

