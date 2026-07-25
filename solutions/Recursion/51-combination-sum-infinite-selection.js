class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def recur(i, sm, path):
            if sm > target:
                return

            if sm == target:
                result.append(path[:])
                return
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                recur(j, sm+candidates[j], path)
                path.pop()
        
        recur(0, 0, [])
        return result
            
        