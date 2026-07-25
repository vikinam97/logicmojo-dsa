from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # @cache
        # def recur(i, j):
        #     if i > m or j > n:
        #         return 0

        #     if i == m-1 and j == n-1:
        #         return 1
            
        #     return recur(i, j+1) + recur(i+1, j)
        
        # return recur(0, 0)

        # dp = [ [0] * n for _ in range(m) ]
        # for i in range(n):
        #     dp[0][i] = 1
        # for j in range(m):
        #     dp[j][0] = 1
        
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
        # return dp[-1][-1]

        
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
        
        for i in range(1, m):
            dp2 = [0] * n
            dp2[0] = 1
            for j in range(1, n):
                dp2[j] = dp2[j-1] + dp[j]
            dp = dp2
            
        return dp[-1]


        

        