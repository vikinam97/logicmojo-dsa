class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = 0, 0
        e1, e2 = None, None
        for num in nums:
            if c1 == 0 and e2 != num:
                c1, e1 = 1, num
            elif c2 == 0 and e1 != num:
                c2, e2 = 1, num
            elif e1 == num:
                c1 += 1
            elif e2 == num:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == e1: count1 += 1
            if num == e2: count2 += 1
        
        result = []
        if count1 > (len(nums)//3): result.append(e1)
        if count2 > (len(nums)//3): result.append(e2)

        return result