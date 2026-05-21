# tc = O(N)
# sc = O(1)
# Vignesh
# two pointer
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j >= len(t) or t[j] != s[i]:
                return False
            i += 1
            j += 1
        return i == len(s)