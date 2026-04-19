class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minEle=math.inf
        while l<=r:
            mid=(l+r)//2
            minEle=min(minEle,nums[mid])
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
        return minEle