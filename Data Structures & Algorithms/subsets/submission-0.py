class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curarr=[]
        n=len(nums)
        def backtrack(curarr,index):
            if curarr not in res:
                res.append(curarr.copy())
            if index<n:
                curarr.append(nums[index])
                backtrack(curarr,index+1)
                curarr.pop()
                backtrack(curarr,index+1)
        backtrack(curarr,0)
        return res