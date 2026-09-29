class Solution:
    def maxScore(self, s: str) -> int:
        # to get the maxium score, you want to do such that most of the zeros in the left and most of the 1s in the right
        l=1 if s[0]=='0' else 0
        r=0 
        for i in range(1,len(s)):
            if s[i]=='1':
                r+=1
        res=0
        res=max(res,l+r)

        for i in range(1,len(s)-1):
            if s[i]=='0':
                l+=1
            elif s[i]=='1':
                r-=1
            print(f"l{l}")
            print(f"r{r}")
            res=max(res,l+r)
        return res