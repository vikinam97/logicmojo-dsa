from collections import defaultdict

class Solution:
    # tc = O(n)
    # sc = O(1)
    def sortColors(self, nums: List[int]) -> None:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for i in range(count[0]):
            nums[i] = 0
        for i in range(count[1]):
            nums[count[0] + i] = 1
        for i in range(count[2]):
            nums[count[0] + count[1] + i] = 2
        return nums

    # tc = O(n)
    # sc = O(1)
    def sortColors1(self, nums: List[int]) -> None:
        n = len(nums)
        i, j, k = 0, 0, n-1
        while j <= k:
            if nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
        return nums