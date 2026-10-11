class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        prefix = [0] * n

        prefix[-1] = prices[-1]
        for i in reversed(range(n-1)):
            prefix[i] = max(prefix[i+1], prices[i])

        result = 0

        for i in range(n):
            result = max(
                result,
                prefix[i] - prices[i]
            )

        return result
