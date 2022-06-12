import unittest
from typing import *

# https://leetcode.com/contest/weekly-contest-297/problems/minimum-path-cost-in-a-grid/

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        """
        첫 번째 row 부터 시작하여, 
        다음 row 의 어떤 cell 로 갈지 결정

        dp 로 풀어야 할 듯?

        dp[row][col] -> row, col 까지 도달하는 가장 저렴한 비용 

        recurrence relation -> 

        dp[row][col_target] = min(dp[row-1][col_src] + moveCost[grid[row-1][col_src]][col_target] for col_src in range(len(grid[row-1])))

        base cases -> 
        dp[0] = moveCost[0]

        answer => min(dp[-1])
        """

        # dp 를 [grid[0]] + [[-1] * len(grid[0])] * len(grid) 로 했더니, row 1 부터 row n 까지 list가 모두 같은것을 바라보게 되어서 에러 났음.
        # 리스트 오브젝트에 대해 곱하기 연산자를 사용할 경우 -> reference 가 복사 되어 버린다. 
        # 아래와 같이 list comp 를 사용해서 list 를 복사해야 이번과 같은 문제가 발생하지 않는다. 
        dp = [grid[0]] + [[-1] * len(grid[0]) for _ in range(len(grid) - 1)]
        for row in range(1, len(grid)):
            for col_target in range(0, len(grid[0])):
                dp[row][col_target] = min((dp[row-1][col_src] + moveCost[grid[row-1][col_src]][col_target]) for col_src in range(len(grid[0]))) + grid[row][col_target]
        
        return min(dp[-1])


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        grid = [[5,3],[4,0],[2,1]]

        # moveCost[i][j] -> cell value 가 i 인 cell 에서 다음 row 의 j 번째 column cell 로 이동하는데 드는 비용
        moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
        answer = 17
        result = self.sol.minPathCost(grid, moveCost)
        self.assertEqual(answer, result)

    def test_example_2(self):
        grid = [[5,1,2],[4,0,3]]
        moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]
        answer = 6
        result = self.sol.minPathCost(grid, moveCost)
        self.assertEqual(answer, result)

    def test_example_3(self):
        grid = [[28,35,29,5,13,17,18,23,14],[30,15,12,27,2,26,25,19,7],[1,16,34,21,9,3,20,24,8],[4,33,22,11,31,0,6,10,32]]
        moveCost = [[87,46,11,33,55,26,26,56,23],[77,56,72,49,35,18,37,66,37],[54,40,62,1,64,49,95,81,77],[80,7,76,71,91,67,75,84,52],[65,11,13,15,9,34,10,98,20],[1,95,100,61,33,47,28,100,44],[39,56,94,7,64,91,66,34,70],[37,99,62,7,23,78,74,89,97],[84,41,63,42,84,15,46,31,11],[60,36,27,25,37,18,4,90,43],[35,83,90,37,91,27,61,99,53],[85,2,98,99,67,70,38,91,68],[66,46,7,99,26,81,95,51,51],[41,96,66,84,61,73,78,28,63],[38,34,49,55,35,29,93,5,28],[3,30,80,20,23,10,93,40,33],[8,86,47,15,45,84,47,19,58],[72,5,76,82,60,50,13,74,38],[4,8,25,38,29,4,60,81,21],[65,50,74,32,9,47,71,55,14],[90,30,92,51,45,51,4,85,22],[30,56,1,45,63,72,91,73,60],[51,61,53,49,44,99,11,5,3],[24,54,91,11,5,30,50,89,44],[87,97,46,92,93,41,64,73,15],[94,76,90,80,30,9,88,8,33],[50,34,4,63,49,90,46,55,16],[10,46,80,21,97,69,70,85,31],[10,66,74,43,65,45,85,34,91],[82,26,77,10,2,5,89,39,4],[80,70,89,73,54,61,100,89,23],[30,66,80,51,3,34,92,100,63],[74,15,4,33,37,3,87,76,92],[44,43,77,99,27,1,23,10,8],[8,74,17,35,31,84,97,98,34],[99,9,28,43,55,39,93,64,93]]
        answer = 59
        result = self.sol.minPathCost(grid, moveCost)
        self.assertEqual(answer, result)
    
if __name__ == '__main__':
    unittest.main()


    


