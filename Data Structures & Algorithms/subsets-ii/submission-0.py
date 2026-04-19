class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        def dfs(i,arr):
            if i==len(nums):
                res.append(arr.copy())
            if i>=len(nums):
                return
            arr.append(nums[i])
            dfs(i+1,arr)
            arr.pop()
            while i<len(nums)-1 and (nums[i]==nums[i+1]):
                i+=1
            dfs(i+1,arr)
            

        dfs(0,[])
        return res
