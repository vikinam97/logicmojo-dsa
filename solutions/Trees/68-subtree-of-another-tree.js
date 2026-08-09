# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def inorder(node, path):
            if not node:
                path.append('N')
                return
            
            path.append('(')
            path.append(str(node.val))
            inorder(node.left, path)
            inorder(node.right, path)
            path.append(')')
        
        main, sub = [], []
        inorder(root, main)
        inorder(subRoot, sub)
        main = "".join(main)
        sub = "".join(sub)

        return sub in main



        