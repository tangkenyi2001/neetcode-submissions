import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]

        def bt(i):
            if i>=len(nums):
                return
            if sum(cur)==target:
                res.append(copy.deepcopy(cur))
                return
            elif sum(cur)>target:
                return
            cur.append(nums[i])
            bt(i)
            cur.pop()
            #it needs to be different and within range
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            bt(i+1)
        bt(0)
        return res


