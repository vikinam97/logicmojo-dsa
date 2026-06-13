# TC = nLogn
# SC = n
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [
            (position[i], speed[i]) for i in range(len(position))
        ]

        cars.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for p, s in cars:
            at = ((target - p) / s)
            if not stack:
                stack.append(at)
                continue
            
            if stack[-1] < at:
                stack.append(at)

        return len(stack)
        