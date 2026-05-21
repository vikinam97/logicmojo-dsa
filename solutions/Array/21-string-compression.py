# tc = O(N)
# sc = O(1)
# Vignesh
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        i = 0
        while i < len(chars):
            j = i
            while j+1 < len(chars) and chars[j] == chars[j+1]:
                j += 1
            
            grpLen = j - i + 1
            compressed = ""
            if grpLen == 1:
                compressed = chars[i]
            else:
                compressed = chars[i] + str(grpLen)

            for c in compressed:
                chars[count] = c
                count += 1

            i = j+1
        return count