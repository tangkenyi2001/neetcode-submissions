class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        first=0
        length=len(nums)
        res=[]
        while first<length:
            l=first+1
            r=length-1
            while l<r:
                if nums[first]+nums[l]+nums[r]==0:
                    res.append([nums[first],nums[l],nums[r]])
                    #shift l now
                    r-=1
                    while l+1<length and  nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                elif nums[first]+nums[l]+nums[r]<0:
                    l+=1 
                else:
                    r-=1
            
            while first+1<length and  nums[first]==nums[first+1]:
                first+=1    
            first+=1
        return res
