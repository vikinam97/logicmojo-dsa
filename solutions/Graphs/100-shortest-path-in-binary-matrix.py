import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        bfs = [(1, 0, 0)]
        seen = set()

        while bfs:
            d, i, j = heapq.heappop(bfs)

            if i == m-1 and j == n-1:
                return d
            
            if (i, j) in seen:
                continue
            seen.add((i, j))

            for di, dj in dirs:
                ni, nj = i+di, j+dj

                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                
                if grid[ni][nj] != 0:
                    continue
                
                heapq.heappush(bfs, (d + 1, ni, nj))
        
        return -1
            




                
