class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices) - 1:
            if prices[r] < prices[l]:
                l = r
            r += 1
            maxP = max(maxP, prices[r] - prices[l])
        return maxP
