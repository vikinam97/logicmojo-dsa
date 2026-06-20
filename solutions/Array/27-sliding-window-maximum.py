# Time - O(N)
# Space - O(K)
# deque and monotonic decreasing 

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        win = deque()
        for i in range(min(n, k)):
            while win and win[-1][1] < nums[i]:
                win.pop()
            win.append((i, nums[i]))
        
        res = [win[0][1]]
        for i in range(k, n):
            while win and win[-1][1] < nums[i]:
                win.pop()
            win.append((i, nums[i]))

            while win and win[0][0] <= (i - k):
                win.popleft()
            
            res.append(win[0][1])

        return res

        