# Time - O(N)
# Space - O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        sm = 0
        for num in nums:
            if sm < 0:
                sm = 0
            sm += num
            result = max(sm, result) 
        return result