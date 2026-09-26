class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        b = nums[-1]
        a = max(nums[-2], b)

        for i in reversed(range(n - 2)):
            c = max(
                b + nums[i],
                a
            )
            a, b = c, a

        return a


        # dp = [ nums[i] for i in range(n) ]
        # dp[-2] = max(nums[-1], nums[-2])

        # for i in reversed(range(n-2)):
        #     dp[i] = max (
        #         dp[i+2] + nums[i],
        #         dp[i+1]
        #     )
        
        # return dp[0]

        # def recur(i):
        #     if i >= n:
        #         return 0
            
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = max(
        #         recur(i+2) + nums[i],
        #         recur(i+1)
        #     )

        #     return dp[i]
        
        # return recur(0)
        