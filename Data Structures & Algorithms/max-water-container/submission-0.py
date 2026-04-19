class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxwater=0
        while l<r:
            width=r-l
            maxwater=max(maxwater,width*min(heights[l],heights[r]))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxwater
