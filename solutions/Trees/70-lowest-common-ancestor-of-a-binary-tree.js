# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathp, pathq = [], []

        def dfs(node, target, path):
            if not node:
                return

            path.append(node)
            if node.val == target.val:
                return True
            
            if dfs(node.left, target, path):
                return True
            if dfs(node.right, target, path):
                return True
            
            path.pop()
        
        dfs(root, p, pathp)
        dfs(root, q, pathq)
        
        hsh = set(pathp)

        for u in reversed(pathq):
            if u in hsh:
                return u

        return None