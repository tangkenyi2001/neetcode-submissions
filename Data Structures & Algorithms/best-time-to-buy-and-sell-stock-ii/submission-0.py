class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        profit=0
        while r<len(prices):
            curPrice=prices[r]-prices[l]
            if curPrice>0:
                profit+=curPrice
            l=r
            r+=1
        return profit