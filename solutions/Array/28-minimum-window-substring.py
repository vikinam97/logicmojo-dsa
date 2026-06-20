from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare(a, b):
            for k in a:
                if k not in b or a[k] > b[k]:
                    return False
            return True

        ht = defaultdict(int)
        for char in t:
            ht[char] += 1
        
        hs = defaultdict(int)
        i, j = 0, 0
        minWin = len(s)
        res = None

        while j < len(s):
            char = s[j]
            hs[char] += 1

            while i <= j and compare(ht, hs):
                if minWin >= (j-i+1):
                    minWin = j-i+1
                    res = (i, j)
                hs[s[i]] -= 1
                i += 1

            j+=1

        return s[res[0]:res[1]+1] if res != None else ""
            


        