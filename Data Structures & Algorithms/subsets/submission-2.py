import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        def bt(i):
            #define ending case
            #if i > than the last 
            if i>=(len(nums)):
                res.append(copy.deepcopy(cur))
                return
            cur.append(nums[i])
            bt(i+1)
            cur.pop()
            bt(i+1)

        bt(0)
        return res