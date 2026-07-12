class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def recur(i, sm):
            if i >= len(nums):
                return 1 if sm == target else 0
            if (i, sm) in dp:
                return dp[(i, sm)]
            
            dp[(i, sm)] = recur(i+1, sm + nums[i]) + recur(i+1, sm - nums[i])

            return dp[(i, sm)]

        return recur(0, 0)