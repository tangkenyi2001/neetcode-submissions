class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        length=len(candidates)
        candidates=sorted(candidates)
        def backtrack(cur,i):
            if sum(cur)==target:
                res.append(cur.copy())
                return
            if i>=length or sum(cur)>target:
                return
            cur.append(candidates[i])
            backtrack(cur,i+1)
            cur.pop()
            while i+1<length and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(cur,i+1)
        backtrack(cur,0)
        return res
