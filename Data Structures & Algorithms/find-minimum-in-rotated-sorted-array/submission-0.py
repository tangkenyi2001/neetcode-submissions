class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minlength=math.inf
        while l<=r:
            mid=(l+r)//2
            if nums[r]>nums[mid]:
                r=mid-1
            else:
                l=mid+1
            minlength=min(minlength,nums[mid])
        return minlength