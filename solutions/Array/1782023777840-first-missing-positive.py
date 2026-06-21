# Time - O(N)
# Space - O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        junk = len(nums)+1

        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = junk
        for num in nums:
            idx = abs(num)-1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return junk 