class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [ (['.'] * n) for _ in range(n)]

        col = set()
        reverseDiag = set()
        diagonal = set()

        result = []
        def recur(i):
            if i >= n:
                temp = []
                for k in range(n):
                    temp.append("".join(grid[k]))
                result.append(temp)
                return
            
            for j in range(n):
                if j in col or (i-j) in diagonal or (i+j) in reverseDiag:
                    continue
                col.add(j)
                reverseDiag.add(i+j)
                diagonal.add(i-j)
                grid[i][j] = 'Q'

                recur(i+1)

                col.remove(j)
                reverseDiag.remove(i+j)
                diagonal.remove(i-j)
                grid[i][j] = '.'
        
        recur(0)

        return len(result)

        