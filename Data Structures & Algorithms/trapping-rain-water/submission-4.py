class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        rightheight=height[r]
        leftheight=height[l]
        trapwater=0
        while l<r:
            if leftheight<rightheight:
                l+=1
                leftheight=max(leftheight,height[l])
                trapwater+=leftheight-height[l]

            else:
                r-=1
                rightheight=max(rightheight,height[r])
                trapwater+=rightheight-height[r]

        return trapwater
