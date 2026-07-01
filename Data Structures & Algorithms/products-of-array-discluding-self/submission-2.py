class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        cur=1
        res=[1]*length
        for i in range(length):
            res[i]=cur
            cur=cur*nums[i]
        cur=1
        for j in range(length-1,-1,-1):
            res[j]=res[j]*cur
            cur=cur*nums[j]
        return res