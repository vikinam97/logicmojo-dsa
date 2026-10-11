class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        grid = [[ 0 for _ in range(W+1) ] for _ in range(n)]
        
        for w in range(W+1):
            if w >= wt[0]:
                grid[0][w] = val[0]
        
        for i in range(1, n):
            for w in range(1, W+1):
                not_take = grid[i-1][w]
                take = 0
                
                if w-wt[i] >= 0:
                    take = val[i] + grid[i-1][w-wt[i]]
                    
                grid[i][w] = max(
                     take,
                     not_take
                    )
        
        return grid[n-1][W]
                    