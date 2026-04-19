class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        res=0
        for i in nums:
            if i-1 not in numsset:
                length=1
                while i+length in numsset:
                    length+=1
                res=max(res,length)
        return res