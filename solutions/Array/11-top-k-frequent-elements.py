from collections import defaultdict
from typing import List

class Solution:
    # tc = O(nlogk)
    # sc = O(k)
    # using heap
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        hsh = defaultdict(int)

        for n in nums:
            hsh[n] += 1
        
        freqList = []
        for n in hsh:
            freqList.append((n, hsh[n]))
        
        freqList.sort(key=lambda x: x[1])
        
        result = freqList[len(freqList) - k:]
        
        return [n for n, count in result]

    # tc = O(n)
    # sc = O(n)
    # bucket sort using frequency hash other than list
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = defaultdict(int)

        for n in nums:
            hsh[n] += 1
        
        freqHsh = defaultdict(list)
        maxFreq = float('-inf')
        for n in hsh:
            freqHsh[hsh[n]].append(n)
            maxFreq = max(maxFreq, hsh[n])
        
        result = []
        for i in reversed(range(maxFreq+1)):
            if i not in freqHsh: continue
            if len(result) >= k: break

            result.extend(freqHsh[i])
        
        return result