import unittest
from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        2,7,11,15 에서 9를 만들 수 있는 두 idx 찾기 (중복 안됨.)
        two pointer approach? 

        2, 15 에서 시작해서 합쳐본다 -> 17 -> 9보다 큼. -> 큰쪽을 작게 만들어야 가능성이 있음 
        2, 11 == 13 -> 9 보다 큼 
        2, 7 == 9 -> 정답 

        >> 즉 두 수를 더 했을 때 값을 가지고 l, r 중 어디를 움직일지 결정한다. 
        두 수의 합이 타깃보다 작을 경우 작은쪽 (l) 을 움직이고  더 클 경우 큰 쪽 (r) 을 움직인다. 

        >> 반례? 

        반례라고 한다면 정답을 찾기 위해서, 합이 타깃보다 작은데, 오히려 l 을 더 큰쪽으로 움직여야 한다거나, 그 반대의 경우라는 것임. 
        없음. 일단 큰쪽부터 줄여놓고 그 다음에 작은쪽을 움직여야할 때 움직이면 됨. 

        """
        l, r = 0, len(numbers) - 1

        while True:
            v_l, v_r = numbers[l], numbers[r]

            if v_l + v_r == target:
                return [l + 1, r + 1]
            elif v_l + v_r < target:
                l += 1
            else:
                r -= 1



class SolutinTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def tests(self):
        tc = [
            ([2,7,11,15], 9, [1,2]),
            ([2,3,4], 6, [1,3]),
            ([-1, 0], -1, [1,2])
        ]

        for idx, _tc in enumerate(tc):
            with self.subTest(idx=idx):
                numbers = _tc[0]
                target = _tc[1]
                answer = _tc[2]
                result = self.sol.twoSum(numbers, target)
                self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()