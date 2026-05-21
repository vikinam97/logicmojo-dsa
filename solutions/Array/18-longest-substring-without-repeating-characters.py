# tc = O(N)
# sc = O(1)
# Vignesh
# two pointer
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        i, j = 0, 0
        result = 0
        while j < len(s):
            char = s[j]

            while char in window and window[char] > 0:
                window[s[i]] -= 1
                i += 1
            window[char] += 1
            
            result = max(result, j-i+1)
            
            j += 1
        return result
        