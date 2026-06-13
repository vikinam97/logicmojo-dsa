from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        dm = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
        d = 0
        i, j = 0, 0
        r, c = len(matrix), len(matrix[0])
        result = []
        seen = set()
        
        result.append(matrix[i][j])
        seen.add((i, j))
        
        if len(result) == r * c:
            return result

        while True:
            dx, dy = dm[d]
            ni, nj = i + dx, j + dy

            if ni >= r or ni < 0 or nj >= c or nj < 0 or (ni, nj) in seen:
                d = (d + 1) % 4
                continue

            i, j = ni, nj
            result.append(matrix[i][j])
            seen.add((i, j))
            
            if len(result) == r * c:
                break
        
        return result