# Time - O(m * n)
# space - O(n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[i] = 1
        
        for i in range(1, m):

            nxtdp = [0] * n
            nxtdp[0] = dp[0] if obstacleGrid[i][0] == 0 else 0

            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                nxtdp[j] = nxtdp[j-1] + dp[j]
            
            dp = nxtdp

        return dp[-1]