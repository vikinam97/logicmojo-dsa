# Time - O(V+E)
# Space - O(V+E)

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjList = [ [] for _ in range(numCourses) ]
        req = [ 0 ] * numCourses

        for u, v in prerequisites:
            adjList[v].append(u)
            req[u] += 1
        
        bfs = deque([])

        for i, count in enumerate(req):
            if count == 0:
                bfs.append(i)
        
        seen = set()

        while bfs:
            course = bfs.popleft()
            seen.add(course)

            for nextCourse in adjList[course]:
                if nextCourse in seen:
                    continue

                req[nextCourse] -= 1
                if req[nextCourse] != 0:
                    continue

                seen.add(nextCourse)
                bfs.append(nextCourse)
        
        return len(seen) == numCourses


