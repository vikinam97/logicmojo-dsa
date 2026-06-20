# Time - O(N)
# Space - O(N)
from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        hsh = defaultdict(int)
        for i, num in enumerate(nums):
            if hsh[(k - num)] > 0:
                count += 1
                hsh[k-num] -= 1
            else:
                hsh[num] += 1
        
        return count