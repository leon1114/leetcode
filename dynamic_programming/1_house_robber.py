import math
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1) subproblem definition
        - dp[n] -> n 번째 집까지 고려했을때 최대 수익 
        
        2) recurrence relation 
        - dp[n] = max(dp[n-1], dp[n-2] + nums[n])
        
        3) base case 
        dp[0] = nums[0]

        Runtime: 38 ms, faster than 71.93% of Python3 online submissions for House Robber.
        Memory Usage: 14 MB, less than 18.73% of Python3 online submissions for House Robber.
        """
        if len(nums) <= 2:
            return max(nums)
        
        n_2 = nums[0]
        n_1 = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            ans = max(n_1, n_2 + nums[i])
            n_1, n_2 = ans, n_1
        
        return ans