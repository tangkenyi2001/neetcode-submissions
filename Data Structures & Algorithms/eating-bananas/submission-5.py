class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #max k u can have is the max(of piles)
        r=max(piles)
        l=1
        while l<=r:
            mid=(r+l)//2
            counter=0
            for i in piles:
                counter+=math.ceil(i/mid)
            if counter>h:
            #if cannot finish, increase k
                l=mid+1
            else:
            #if can finish, reduce k
                r=mid-1
        return l