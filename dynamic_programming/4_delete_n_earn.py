import unittest
from typing import *

from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """

        subprolem -> dp[i] -> index i 까지 고려했을때 최대값 
        recurrence -> dp[i] => max(dp) or max(dp[:i-1]) if abs(num - nums[i-1]) <=

        이미 정렬된 상태라면, nums[i] 값을 이용해 다음 것을 선택할 수 있을지 없을지 알 수 있다. 

        base -> 
        dp[0] -> dp[0] * count(0)
        dp[1] -> 
        """
        if len(nums) == 1:
            return nums[0]

        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        
        nums = sorted(list(set(nums)))

        if len(nums) == 1:
            return nums[0] * nums_count[nums[0]]

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0] * nums_count[nums[0]]
        dp[1] = nums[1] * nums_count[nums[1]] + (0 if abs(nums[0] - nums[1]) == 1 else dp[0])

        for idx in range(2, len(nums)):
            num = nums[idx]
            if abs(num - nums[idx-1]) == 1:
                _max = num * nums_count[num] + max(dp[:idx-1])
            else:
                _max = max(dp) + num * nums_count[num]
            dp[idx] = _max

        return max(dp)


class SolutionTests(unittest.TestCase):
    def tests(self):
        sol = Solution()

        tc = [
            # ([3,4,2], 6),
            # ([2,2,3,3,3,4], 9),
            ([1,1,1,2,4,5,5,5,6], 18)
        ]

        for t in tc:
            with self.subTest():
                self.assertEqual(sol.deleteAndEarn(t[0]), t[1])


if __name__ == '__main__':
    unittest.main()