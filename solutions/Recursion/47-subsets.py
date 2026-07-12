class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recur(i, path):
            if i >= len(nums):
                return result.append(path[:])

            path.append(nums[i])
            recur(i + 1, path)
            path.pop()

            recur(i + 1, path)
        recur(0, [])
        return result