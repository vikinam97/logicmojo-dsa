from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        # def recur(i):
        #     if i < 0:
        #         return 0

        #     if i == 0:
        #         return 1
            
        #     return recur(i - 1) + recur(i - 2)
        
        # return recur(n)

        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[-1]

        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b


        