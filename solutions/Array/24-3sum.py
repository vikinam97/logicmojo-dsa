# Time = O(N^2)
# Space = O(1)
# use set to ignore duplicates results
class Solution1:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        hsh = set()
        for i in range(n-2):

            j, k = i+1, n-1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if (sm) == 0:
                    if (nums[i], nums[j], nums[k]) not in hsh:
                        result.append([nums[i], nums[j], nums[k]])
                    hsh.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                elif sm < 0:
                    j += 1
                else:
                    k -= 1
            
        
        return result
        

# Time = O(N^2)
# Space = O(1)
# ignore duplicate in list
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i+1, n-1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if (sm) == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # Move pointers past any duplicate values to avoid duplicates in result
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                        
                    # Crucial: Move both pointers inward after finding a match
                    j += 1
                    k -= 1
                
                elif sm < 0:
                    j += 1
                else:
                    k -= 1
            
        
        return result
        