# tc - O(N)
# sc - O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            sm = numbers[i] + numbers[j]
            if sm > target:
                j -= 1
            elif sm < target:
                i += 1
            else:
                return [i+1, j+1]
        return -1