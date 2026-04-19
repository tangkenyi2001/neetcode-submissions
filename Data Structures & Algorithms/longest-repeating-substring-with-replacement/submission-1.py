class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=set(s)
        length=0
        for i in c:
            l=r=count=0
            while r<len(s):
                if s[r]==i:
                    count+=1
                while (r-l+1-count>k):
                    if s[l]==i:
                        count-=1
                    l+=1
                length=max(length,r-l+1)
                r+=1
                
        return length