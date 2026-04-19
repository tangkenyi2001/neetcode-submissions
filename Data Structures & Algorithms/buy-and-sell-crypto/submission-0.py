class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        cur=0
        length=len(prices)
        nextday=cur+1
        while cur<length and nextday<length:
            #if the next day is lt/et the current day, then the cur should increase
            if nextday<length and prices[nextday]<=prices[cur]:
                cur=nextday

            #if the next day is greater, keep current and continue iterating
            elif nextday<length and prices[nextday]>prices[cur]:
                profit=max(profit,prices[nextday]-prices[cur])
            nextday+=1
        return profit