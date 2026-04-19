class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def bt(i,cur,total):
            #terminating factor
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return

            cur.append(candidates[i])
            bt(i+1,cur,total+candidates[i])
            cur.pop()
            #cannot be using the same as the prev
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            bt(i+1,cur,total)
        bt(0,[],0)
        return res