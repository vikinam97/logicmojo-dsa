class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        mx_sm = sum(nums)
        if mx_sm < target or -mx_sm > target:
            return 0

        n = len(nums)

        dp = [ 0 for _ in range( 2*mx_sm + 1) ]

        dp[mx_sm] = 1

        for i in range(0, n):
            ndp = [ 0 for _ in range( 2*mx_sm + 1) ]
            for j in range( 2* mx_sm+1):
                if dp[j] == 0:
                    continue
                
                ndp[ (j - mx_sm) + nums[i] + mx_sm] += dp[j]
                ndp[ (j - mx_sm) - nums[i] + mx_sm] += dp[j]
            dp = ndp

        return dp[mx_sm + target]


        # mx_sm = sum(nums)
        # if mx_sm < target or -mx_sm > target:
        #     return 0

        # n = len(nums)

        # dp = [ [ 0 for _ in range( 2*mx_sm + 1) ] for _ in range(n+1) ]

        # dp[0][mx_sm] = 1

        # for i in range(0, n):
        #     for j in range( 2* mx_sm+1):
        #         if dp[i][j] == 0:
        #             continue
                
        #         dp[i+1][ (j - mx_sm) + nums[i] + mx_sm] += dp[i][j]
        #         dp[i+1][ (j - mx_sm) - nums[i] + mx_sm] += dp[i][j]

        # return dp[n][mx_sm + target]
        
        
        
        
        
        
        
        
        
        
        
        
        # dp = {}
        # n = len(nums)

        # def recur(i, sm):

        #     if (i, sm) in dp:
        #         return dp[(i, sm)]

        #     if i >= n:
        #         return 1 if sm == 0 else 0
            
        #     dp[(i, sm)] = recur(i+1, sm+nums[i]) + recur(i+1, sm-nums[i])

        #     return dp[(i, sm)]
        
        # return recur(0, target)            