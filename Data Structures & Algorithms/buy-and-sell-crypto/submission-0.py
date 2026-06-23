class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        maxsum = 0

        while p2 < len(prices):
            if prices[p2] - prices[p1] > maxsum:
                maxsum = prices[p2] - prices[p1]
            elif prices[p1] > prices[p2]:
                p1 = p2
            p2+=1
        return maxsum
                
