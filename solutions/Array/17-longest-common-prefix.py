# tc = O(N*M)
# SC = O(1)
# Vignesh
# vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        i = 0
        while True:
            if i >= len(strs[0]):
                break
            
            t = strs[0][i]
            flag = False
            for strng in strs:
                if i >= len(strng) or t != strng[i]:
                    flag = True
                    break

            if flag: break
            i += 1

        return strs[0][:i] if i != -1 else ""