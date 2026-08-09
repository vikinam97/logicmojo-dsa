class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        bfs = [root]
        levels = []
        dr = 1

        while bfs:
            level = []
            nxt_level = []
            for node in bfs:
                level.append(node.val)

                if node.left: nxt_level.append(node.left)
                if node.right: nxt_level.append(node.right)
            
            levels.append(level if dr == 1 else level[::-1])
            dr = 1 if dr == -1 else -1
            bfs = nxt_level
        
        return levels

