class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #first digit is always 0
        res=0
        for i in range(len(nums)+1):
            res^=i
        for j in nums:
            res^=j
        return res
