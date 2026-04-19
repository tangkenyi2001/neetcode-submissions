class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        leftmax[0]=height[0]
        rightmax[-1]=height[-1]
        for i in range(1,len(leftmax)):
            leftmax[i]=max(leftmax[i-1],height[i])
        for i in range(len(rightmax)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        trapwater=0
        for i in range(len(height)):
            trapwater+=min(rightmax[i],leftmax[i])-height[i]
        return trapwater