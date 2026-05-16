# tc - O(n)
# sc - O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        rightPro = [nums[-1]] * n
        for i in reversed(range(n-1)):
            rightPro[i] = rightPro[i+1] * nums[i]

        result = [rightPro[1]] * n
        runningLeftPro = nums[0]

        for i in range(1, n-1):
            result[i] = runningLeftPro * rightPro[i+1]
            runningLeftPro *= nums[i]

        result[-1] = runningLeftPro
            
        
        return result