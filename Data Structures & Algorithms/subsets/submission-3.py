class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        maxlen=len(nums)
        def bt(i):
            if i==(maxlen):
                res.append(cur[:])
                return

            cur.append(nums[i])
            bt(i+1)
            cur.pop()
            bt(i+1)
        bt(0)
        return res
        