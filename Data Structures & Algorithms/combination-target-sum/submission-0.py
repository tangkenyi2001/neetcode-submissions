class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curarr=[]
        n=len(nums)
        def backtracking(curarr,index):
            if sum(curarr)==target:
                res.append(curarr.copy())
                return
            if sum(curarr)>target or index>=n:
                return
            curarr.append(nums[index])
            backtracking(curarr,index)
            curarr.pop()
            backtracking(curarr,index+1)

        backtracking(curarr,0)
        return res
