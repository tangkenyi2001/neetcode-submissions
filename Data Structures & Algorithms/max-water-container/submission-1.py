class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxwater=0
        while l<r:
            maxwater=max(maxwater,min(heights[l],heights[r])*(r-l))
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxwater