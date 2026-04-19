class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #forwardpass
        initialarr=[1 for _ in (nums)]
        prefix=1
        for i in range(1,len(nums)):
            prefix*=nums[i-1]
            initialarr[i]*=prefix
        #backpass
        postfix=1
        for i in range(len(nums)-2,-1,-1):
            postfix*=nums[i+1]
            initialarr[i]*=postfix
        return initialarr

