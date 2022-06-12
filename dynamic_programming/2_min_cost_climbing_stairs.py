from typing import *

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) <= 2:
            return min(cost)

        n_1 = cost[1]
        n_2 = cost[0]

        for i in range(2, len(cost)):
            ans = min(n_1, n_2) + cost[i]
            n_2, n_1 = n_1, ans

        return min(n_2, n_1)

