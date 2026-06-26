class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for num in nums:
            anum = abs(num)
            if nums[anum] < 0:
                return anum
            nums[anum] = -1 * nums[anum]
        return -1
            