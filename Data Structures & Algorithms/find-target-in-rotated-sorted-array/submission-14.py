class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        res=-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                res=mid
                return res
            #if right side greater than left side
            if nums[r]>nums[l]:
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1 
            #if left side greater than right
            else:   
                if nums[l] <= nums[mid]:
                    if target > nums[mid] or target < nums[l]:
                        l = mid + 1
                    else:
                        r = mid - 1
                    
                else:
                    if target < nums[mid] or target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1


        return res