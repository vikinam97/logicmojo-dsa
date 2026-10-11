class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        rn = 0
        for i in range(n):
            if rn < i:
                return False
            rn = max(
                i + nums[i],
                rn
            )
        
        return True
