class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #traverse, and if is more, continue, if less, start from next
        l,r=0,0
        res=nums[0]
        length=len(nums)
        curcount=0
        while r<length:
            curcount+=nums[r]
            res=max(res,curcount)
            if curcount<=0:
                curcount=0
            r+=1
                
                
        return res
            