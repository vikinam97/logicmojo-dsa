# tc = O(log n)
# sc = O(1)
# 1st find pivot and the search element
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, j = 0, n-1
        while i < j:
            mid = i + ((j-i) // 2)
            
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        
        l, h = 0, 0
        if target > nums[-1]:
            l, h = 0, i
        else:
            l, h = i, n-1

        while l < h:
            mid = l + ((h - l) // 2)
            
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
            else:
                h = mid

        return l if nums[l] == target else -1
        
