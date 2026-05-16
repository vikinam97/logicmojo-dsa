# tc - O(n)
# s  - O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        rightMax = [height[-1]] * n
        for i in reversed(range(n-1)):
            rightMax[i] = max(rightMax[i+1], height[i])

        leftMax = [height[0]] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        result = [0] * n
        for i in range(1, n-1):
            l = leftMax[i-1]
            r = rightMax[i+1]
            w = min(l, r) - height[i]

            result[i] = w if w > 0 else 0
        
        return sum(result)
