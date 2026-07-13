class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:



        n, m = len(board), len(board[0])
        row = [set() for i in range(n)]
        col = [set() for i in range(m)]
        sub = [ [set() for j in range(m//3)] for i in range(n//3) ]

        def select(i, j, num):
            row[i].add(num)
            col[j].add(num)
            sub[i//3][j//3].add(num)
            board[i][j] = num
        def deselect(i, j, num):
            row[i].remove(num)
            col[j].remove(num)
            sub[i//3][j//3].remove(num)
            board[i][j] = "."
        def valid(i, j, num):
            return (num not in row[i]) and (num not in col[j]) and (num not in sub[i//3][j//3])

        blanks = []
        for i in range(n):
            for j in range(m):
                num = board[i][j]
                if num == ".":
                    blanks.append((i, j))
                    continue
                select(i, j, num)

        def recur(ind):
            if ind >= len(blanks):
                return True
            i, j = blanks[ind]
            for num in range(1,9+1):
                snum = str(num)
                if valid(i, j, snum):
                    select(i, j, snum)
                    if recur(ind+1):
                        return True
                    deselect(i, j, snum)
        
        recur(0)

        return board