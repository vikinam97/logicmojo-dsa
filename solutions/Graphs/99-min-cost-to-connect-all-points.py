# Time - O(N^2 log N) 
# Space - O(N)

import heapq

class DSU:
    def __init__(self, n):
        self.list = [ i for i in range(n) ]
    
    def find(self, x):
        if self.list[x] == x:
            return x
        
        self.list[x] = self.find(self.list[x])
        return self.list[x]
    
    def is_same_parent(self, x, y):
        px = self.find(x)
        py = self.find(y)

        return px == py

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        
        self.list[px] = py

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                d = abs(x2-x1) + abs(y2-y1)

                edges.append((d, i, j))
        
        edges.sort(key = lambda x: x[0])

        dsu = DSU(n)
        cost = 0

        for w, u, v in edges:
            if dsu.is_same_parent(u, v):
                continue
            
            dsu.union(u, v)
            cost += w

        return cost
