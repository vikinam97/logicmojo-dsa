class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # value -> index
        
        for i, num in enumerate(nums):
            rem = target - num
            # If the complement exists, we found our pair
            if rem in hash_map:
                return [hash_map[rem], i]
            
            # Otherwise, add the current number to the hash map
            hash_map[num] = i
            
        return []