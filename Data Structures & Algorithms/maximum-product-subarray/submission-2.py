class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #so for a number, what is the max, we either * it or we dont
        #brute force is that we do a n*n solution where start from 1 to 4, then sec
        dp=[[nums[i],nums[i]] for i in range(len(nums))]
        #the issue is a negative number can become a positive one after, so it will not be right to skip through.
        # or we store 2 values, the max positive and most negative one
        length=len(nums)
        res=nums[0]
        for i in range(1,length):
            #the max postive one
            dp[i][0]=max(nums[i]*dp[i-1][0],nums[i]*dp[i-1][1],nums[i])
            #the most negative one
            dp[i][1]=min(nums[i]*dp[i-1][0],nums[i]*dp[i-1][1],nums[i])
            res=max(dp[i][0],dp[i][1],res)

        return res
