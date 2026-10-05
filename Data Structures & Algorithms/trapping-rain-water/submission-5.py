class Solution:
    def trap(self, height: List[int]) -> int:
        l=1
        r=len(height)-2
        lmax=height[0]
        rmax=height[-1]
        #essentially, we are trying to compute the amount of water if min(leftmax,right max)>cur
        # the idea is that we always want to move the minimum window
        count=0
        while l<=r:
            if lmax>rmax:
                if min(lmax,rmax)>height[r]:
                    count+=min(lmax,rmax)-height[r]
                rmax=max(rmax,height[r])
                r-=1
            else:
                if min(lmax,rmax)>height[l]:
                    count+=min(lmax,rmax)-height[l]
                lmax=max(lmax,height[l])
                l+=1
        return count
                
