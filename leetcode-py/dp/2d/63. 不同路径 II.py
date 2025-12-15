# 给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。

# 网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

# 返回机器人能够到达右下角的不同路径数量。

# 测试用例保证答案小于等于 2 * 109。

 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # meet obstable return 0
        # out of bound return 0

        # dfs (i, j) -> max unique paths of i, j(Begin from 0, 0)
        # dfs i,j = dfs (i-1, j ) + dfs(i, j-1)

        i_limit = len(obstacleGrid)-1
        j_limit = len(obstacleGrid[0])-1
        memo = [[None for _ in range(j_limit+1)] for _ in range(i_limit+1)]

        if i_limit < 0:
            return 0

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if memo[i][j] is not None:
                return memo[i][j]
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            
            memo[i][j] = dfs(i-1, j) + dfs(i, j-1)
            return memo[i][j]

        return dfs(i_limit, j_limit)


        