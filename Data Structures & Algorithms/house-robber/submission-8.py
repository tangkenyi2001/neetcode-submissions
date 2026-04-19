class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=cur=0
        maxvalue=0
        for i in nums:
            cur=max(cur+i,prev)
            maxvalue=max(maxvalue,cur)
            cur,prev=prev,cur
        return maxvalue