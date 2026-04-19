class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        n=len(candidates)
        candidates=sorted(candidates)
        def backtracking(cur,index):
            #base case
            if sum(cur)==target:
                res.append(cur.copy())
                return
            if sum(cur)>target or index>=n:
                return
            cur.append(candidates[index])
            backtracking(cur,index+1)
            cur.pop()
            while index+1<n and candidates[index]==candidates[index+1]:
                index+=1
            backtracking(cur,index+1)
        backtracking(cur,0)
        return res