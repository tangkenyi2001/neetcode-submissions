class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles = [25,10,23,4], h = 4, to finish in 4 hours worst case if no algo is 25.
        worstcase=max(piles)
        l=1
        mink=worstcase
        while l<=worstcase:
            mid=(worstcase+l)//2
            hours=0
            for i in piles:
                hours+=math.ceil(i/mid)
            #increase the rate of eating
            if hours>h:
                l=mid+1
            #decrease the rate of eating
            else:
                mink=mid
                worstcase=mid-1
        return mink
                
            