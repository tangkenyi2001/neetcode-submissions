class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        #one portion of the arr will be increasing, just have to find that portion
        # four scenarios
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[r]:
                r=mid
            else:
                l=mid+1
        return nums[l]

