class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #so can jump up to 2 boxes if in index 1 [1,2,1,0,1]
        #so should reach index 4 and realise u cant jump anywhere. should have a jump history

        dp=[0 for _ in range(len(nums))]
        dp[0]=1
        for i in range(len(nums)):
            if dp[i]==1:
                for j in range(1,nums[i]+1):
                    if (i+j)<len(nums):
                        dp[i+j]=1
        
        return dp[-1]==1