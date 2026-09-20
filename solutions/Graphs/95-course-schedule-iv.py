# Time - O(N * N)
# Space - O(N * N)

from collections import deque, defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        
        adjList = defaultdict(list)
        req = [0] * numCourses

        for u, v in prerequisites:
            adjList[u].append(v)
            req[v] += 1 

        bfs = deque([])
        reqSet = [ set() for _ in range(numCourses) ]

        for i in range(numCourses):
            if req[i] == 0:
                bfs.append(i)
        
        while bfs:
            course = bfs.popleft()

            for nxtCourse in adjList[course]:
                reqSet[nxtCourse].update(reqSet[course])
                reqSet[nxtCourse].add(course)

                req[nxtCourse] -= 1

                if req[nxtCourse] == 0:
                    bfs.append(nxtCourse)

        result = []
        for u, v in queries:
            result.append(
                u in reqSet[v]
            )

        return result

        

# Time - O(N * N * N)
# Space - O(N * N)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        
        dp = [ [ float('inf') for _ in range(numCourses) ] for _ in range(numCourses) ]
        
        for u,v in prerequisites:
            dp[u][v] = 1

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    c = dp[i][k] + dp[k][j]

                    dp[i][j] = min(dp[i][j], c)
        
        result = []

        for u, v in queries:
            result.append(
                True if dp[u][v] != float('inf') else False
            )

        return result
        