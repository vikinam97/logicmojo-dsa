# Vignesh
# tc - O(n)
# sc - O(1)
# array reversal
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

# Vignesh
# tc - O(n)
# sc - O(1)
# cyclic swaps
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        n = len(nums)
        start, val = 0, -1
        count = 0
        while count < n:
            val = nums[start]
            curr = start

            while True:
                nxt = (curr + k) % n
                val, nums[nxt] = nums[nxt], val
                count += 1
                curr = nxt

                if curr == start:
                    break
            
            start += 1
        return nums

                
                



        