from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        cur=[]


        def bt(i):
            #terminating factor
            if sum(cur)==target:
                res.append(cur.copy())
                return 
            if i>=len(candidates) or sum(cur)>target:
                return

            cur.append(candidates[i])
            bt(i+1)
            cur.pop()
            #cannot be using the same as the prev
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            bt(i+1)
        bt(0)
        return res