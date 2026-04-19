class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        houses=[0]*len(nums)
        houses[0]=nums[0]
        houses[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            houses[i]=max(houses[i-1],houses[i-2]+nums[i])
        return max(houses)
