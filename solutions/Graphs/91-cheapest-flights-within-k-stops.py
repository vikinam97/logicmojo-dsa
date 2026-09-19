# Time - O(EK log VK)
# Space - O(VK)

from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        adjList = defaultdict(list)

        for u, v, price in flights:
            adjList[u].append((v, price))
        
        bfs = [(0, 0, src)]
        seen = [[float('inf')] * (k + 2) for _ in range(n)]
        seen[src] = (0, 0)

        while bfs:
            price, stops, node = heapq.heappop(bfs)

            if node == dst:
                return price

            for nxtNode, nxtPrice in adjList[node]:
                np, ns = nxtPrice + price, stops + 1

                if ns > k+1:
                    continue

                if np < seen[nxtNode][0]:
                    seen[nxtNode] = (np, ns)
                    heapq.heappush(bfs, (np, ns, nxtNode))
                elif ns < seen[nxtNode][1]:
                    heapq.heappush(bfs, (np, ns, nxtNode))
        
        return -1




        