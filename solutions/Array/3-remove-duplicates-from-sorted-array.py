# tc - O(n)
# sc - O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, j = 0, 1
        count = 0
        n = len(nums)

        while j < n:
            if nums[i] == nums[j]:
                j += 1
                continue
            
            count += 1
            i += 1
            nums[i] = nums[j]
        
        return count+1