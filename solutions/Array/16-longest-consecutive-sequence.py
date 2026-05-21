# tc = O(N)
# sc = O(N)
# Vignesh
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)

        curSeen = set()
        result = 0
        for num in nums:
            if num in curSeen:
                continue
            t = num
            count = 0
            while t in seen:
                curSeen.add(t)
                count += 1
                t += 1
            t = num-1
            while t in seen:
                curSeen.add(t)
                count += 1
                t -= 1
            result = max(result, count)
        
        return result
