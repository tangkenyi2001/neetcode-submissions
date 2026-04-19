class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[r]>=nums[mid]:
                #back half sorted
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[mid]>=nums[l]:
                #front half sorted
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            

        return -1