class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxsum = 0;

        for sell in prices:
            maxsum = max(sell - minBuy, maxsum)
            minBuy = min(sell, minBuy)
        return maxsum