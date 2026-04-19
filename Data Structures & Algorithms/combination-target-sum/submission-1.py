class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        def dfs(i,cur):
            if sum(cur)==target:
                res.append(cur.copy())
                return
            elif i>=len(nums) or sum(cur)>target:
                return
            cur.append(nums[i])
            dfs(i,cur)
            cur.pop()
            dfs(i+1,cur)
        dfs(0,cur)
        return res