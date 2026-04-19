class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        length=len(nums)
        def bt(cur):
            #base case when length is tha same as nums
            if len(cur)==length:
                res.append(cur.copy())
                return
            for j in nums:
                if j not in cur:
                    cur.append(j)
                    bt(cur)
                    cur.pop()
        bt(cur)
        return res
