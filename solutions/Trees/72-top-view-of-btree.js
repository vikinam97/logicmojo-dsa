class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def topView(self, root):
        if not root:
            return []

        hsh = {} 
        minx, maxx = 0, 0

        def dfs(node, x, depth):
            nonlocal minx, maxx
            if not node:
                return

            if x not in hsh or depth < hsh[x][1]:
                hsh[x] = (node.data, depth)
                minx = min(x, minx)
                maxx = max(x, maxx)

            dfs(node.left, x - 1, depth + 1)
            dfs(node.right, x + 1, depth + 1)

        dfs(root, 0, 0)

        result = []
        i = minx
        while i <= maxx:
            if i in hsh:
                result.append(hsh[i][0])
            i += 1

        return result