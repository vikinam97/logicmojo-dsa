class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def attachToRightMost(node, toMove):
            while node.right:
                node = node.right
            node.right = toMove

        def recur(node):
            if not node:
                return None

            if node.val > key:
                node.left = recur(node.left)
                return node
            elif node.val < key:
                node.right = recur(node.right)
                return node
            
            if not node.left and not node.right:
                return None
            
            if not node.left:
                return node.right

            if not node.right:
                return node.left
            
            attachToRightMost(node.left, node.right)
            return node.left            
        
        return recur(root)
        