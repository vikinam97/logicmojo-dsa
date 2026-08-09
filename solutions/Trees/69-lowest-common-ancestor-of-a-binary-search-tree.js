# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node:
                return
            
            if node == p or node == q:
                return node
            
            lp = p.val < node.val
            rp = p.val > node.val

            lq = q.val < node.val
            rq = q.val > node.val

            if lp and lq:
                return dfs(node.left, p, q)
            
            if rp and rq:
                return dfs(node.right, p, q)
            
            return node
            
        return dfs(root, p, q)
        