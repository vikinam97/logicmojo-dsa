# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [-1, -1]
            
            if not node.left and not node.right:
                return [0, 0]
            
            [leftMaxPath, leftMaxDia] = dfs(node.left)
            [rightMaxPath, rightMaxDia] = dfs(node.right)

            nodeMaxDia = 0
            if leftMaxPath != None:
                nodeMaxDia += 1 + leftMaxPath
            if rightMaxPath != None:
                nodeMaxDia += 1 + rightMaxPath
            
            return [
                1 + max(leftMaxPath, rightMaxPath),
                max(leftMaxDia, rightMaxDia, nodeMaxDia)
            ]
        
        [_, dia] = dfs(root)
        return dia