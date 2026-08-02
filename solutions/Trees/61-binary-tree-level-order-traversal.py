class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        bfs = [root]
        levels = []

        while bfs:
            level = []
            nextlevel = []

            for node in bfs:
                level.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            
            levels.append(level)
            bfs = nextlevel
        
        return levels