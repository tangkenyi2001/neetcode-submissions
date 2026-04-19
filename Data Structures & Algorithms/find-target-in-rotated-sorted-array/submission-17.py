
class Solution:
    def search(self, nums, target):
        l,r=0,len(nums)-1
        res=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                res=mid
                return res
            #left side sorted
            if nums[mid]>=nums[l]:
                if target>=nums[l] and target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            
            #right side sorted
            else:
                if target<=nums[r] and target>=nums[mid]:
                    l=mid+1
                else:
                    r=mid-1

        return res

            
S=Solution()
print(S.search([3,1],1))