class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(houses):
            maxAmount=0
            prev,cur=0,0
            for house in houses:
                cur=max(cur+house,prev)
                maxAmount=max(maxAmount,cur)
                cur,prev=prev,cur
            return maxAmount
        
        return max(helper(nums[1:]),helper(nums[:-1]))