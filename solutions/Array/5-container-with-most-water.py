# tc = O(n)
# sc = O(1)

class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n-1
        maxSoFar = -1

        while i < j:
            h = min(nums[i], nums[j])
            w = j-i
            area = h * w

            maxSoFar = max(maxSoFar, area)

            if nums[i] < nums[j]:
                i += 1
            else: 
                j -= 1

        return maxSoFar


