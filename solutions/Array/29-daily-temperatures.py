# Time - O(N)
# Space - O(N)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n 

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                j = stack[-1][0]
                result[ j ] = i-j
                stack.pop()
            
            stack.append((i, t))
        
        return result
        