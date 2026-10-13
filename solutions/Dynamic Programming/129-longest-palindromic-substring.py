class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxSoFar = 0
        for p in range(n):
            i, j = p, p
            while i >= 0 and j < n and s[i] == s[j]:
                l = j-i+1
                if maxSoFar < l:
                    maxSoFar = l
                    result = s[i:j+1]
                i -= 1
                j += 1
            i, j = p, p+1
            while i >= 0 and j < n and s[i] == s[j]:
                l = j-i+1
                if maxSoFar < l:
                    maxSoFar = l
                    result = s[i:j+1]
                i -= 1
                j += 1
        return result
        