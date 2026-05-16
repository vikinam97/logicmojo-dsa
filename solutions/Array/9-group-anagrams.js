# N = number of strings, K = max len of string
# tc: O(N * K)
# sc: O(N * K)
# Vignesh
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hasher(s):
            arr = [0] * 26
            for char in s:
                arr[ord(char) - 97] += 1
            return "|".join(str(x) for x in arr)
        
        groups = {}
        result = []
        for s in strs:
            hsh = hasher(s)
            if hsh not in groups:
                grp = []
                result.append(grp)
                groups[hsh] = grp
            groups[hsh].append(s)

        return result