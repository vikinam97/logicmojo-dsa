import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append((v, w))

        bfs = [(0, k)]
        nodeTime = [float('inf')] * n
        nodeTime[k - 1] = 0

        while bfs:
            curTime, node = heapq.heappop(bfs)

            if curTime > nodeTime[node-1]:
                continue 

            for v, w in adjList[node]:
                newTime = curTime + w

                if newTime < nodeTime[v - 1]:
                    nodeTime[v - 1] = newTime
                    heapq.heappush(bfs, ( newTime, v ))

        minTime = max(nodeTime)

        return minTime if minTime != float('inf') else -1