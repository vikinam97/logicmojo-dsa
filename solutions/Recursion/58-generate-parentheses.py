class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recur(o, c, path):
            if o == n and c == n:
                return result.append("".join(path))
            
            if o < n:
                path.append("(")
                recur(o+1, c, path)
                path.pop()
            if c < o:
                path.append(")")
                recur(o, c+1, path)
                path.pop()
        
        recur(0, 0, [])
        return result


        