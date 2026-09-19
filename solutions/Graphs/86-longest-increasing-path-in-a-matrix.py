# Time = O(m*n)
# Space = O(m*n)
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j>= n:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            maxSoFar = 0
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= m or nj < 0 or nj>= n:
                    continue

                if matrix[ni][nj] > matrix[i][j]:
                    maxSoFar = max(dfs(ni, nj), maxSoFar)
            
            memo[(i,j)] = maxSoFar + 1

            return memo[(i,j)]
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result