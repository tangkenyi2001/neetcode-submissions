class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]

        def bt(cur,i):
            if i>=len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            bt(cur,i+1)
            cur.pop()
            bt(cur,i+1)

        bt(cur,0)
        return res