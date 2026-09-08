class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dr = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if grid[i][j] != "1":
                return
            grid[i][j] = -1
            for dx, dy in dr:
                nx, ny = i + dx, j + dy

                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue

                if grid[nx][ny] != "1":
                    continue
                
                dfs(nx, ny)
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
