# tc = O(n)
# sc = O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur:
                count += 1
                continue
            count -= 1
            if count == 0:
                cur = nums[i]
                count = 1
        return cur