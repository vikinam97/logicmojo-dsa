# Vignesh
# tc - O(n)
# sc - O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        n = len(nums)
        while j < n:
            if nums[j] == 0:
                j += 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        return nums