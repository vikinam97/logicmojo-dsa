class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time - O(n*m * max(len(words)))
        # Space - O(p*q)
        
        trie = {}
        m, n = len(board), len(board[0])
        result = {}

        for word in words:
            ttrie = trie
            for c in word:
                if c not in ttrie:
                    ttrie[c] = {}
                ttrie = ttrie[c]
            ttrie['isWord'] = True

        def dfs(i, j, node, seen, path):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            char = board[i][j]
            if (i, j) in seen:
                return

            if char not in node:
                return
            
            seen[(i,j)] = True
            path.append(char)

            if 'isWord' in node[char]:
                result["".join(path)] = True

            
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+di, j+dj

                dfs(ni, nj, node[char], seen, path)

            del seen[(i,j)]
            path.pop() 

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, {}, [])
        
        return list(result)