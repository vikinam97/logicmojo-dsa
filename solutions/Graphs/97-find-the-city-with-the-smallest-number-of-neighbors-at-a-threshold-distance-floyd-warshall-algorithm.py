# Time - O(N^3) 
# Space - O(N^2)

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:

        dp = [ [ float('inf') for _ in range(n) ] for _ in range(n) ]

        for i in range(n):
            dp[i][i] = 0

        for u, v, w in edges:
            dp[u][v] = w
            dp[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d = dp[i][k] + dp[k][j]

                    dp[i][j] = min(dp[i][j], d)

        minCities = n+1
        city = None

        for i in range(n):
            cityCount = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    cityCount += 1
            if cityCount <= minCities:
                minCities = cityCount
                city = i

        return city
        