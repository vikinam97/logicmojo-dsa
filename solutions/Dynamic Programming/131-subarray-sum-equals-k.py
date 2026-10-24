from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        seen = defaultdict(int)
        seen[0] += 1

        count = 0
        for i in range(n):
            t = prefixSum[i] - k

            if t in seen:
                count += seen[t]

            seen[prefixSum[i]] += 1 
        
        return count


        