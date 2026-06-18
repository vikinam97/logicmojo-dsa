# Time = O(M)
# SPace = O(1) ~ O(26)

from collections import defaultdict
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def compare(h1, h2):
            for c in h1:
                if h1[c] != h2[c]:
                    return False
            return True

        hsh = defaultdict(int)
        for c in s1:
            hsh[c] += 1
            
        i = 0
        win = defaultdict(int)
        for j in range(len(s2)):
            c = s2[j]
            
            if c not in hsh:
                i = j
                win = defaultdict(int)
                continue
            
            win[c] += 1
            while win[c] > hsh[c]:
                win[s2[i]] -= 1
                i += 1
            
            if compare(hsh, win):
                return True
        
        return False

# Better - same time but clean
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency map for s1
        hsh = defaultdict(int)
        for c in s1:
            hsh[c] += 1
            
        win = defaultdict(int)
        i = 0 
        
        for j in range(len(s2)):
            c = s2[j]
            win[c] += 1
            
            while win[c] > hsh[c]:
                win[s2[i]] -= 1
                i += 1
            
            if j - i + 1 == len(s1):
                return True
        
        return False