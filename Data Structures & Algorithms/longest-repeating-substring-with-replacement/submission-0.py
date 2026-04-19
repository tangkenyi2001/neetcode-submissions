class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #only upper case english characters
        c=set(s)
        length=0
        for i in c:
            count=l=r=0
            while r<len(s):
                if s[r]==i:
                    count+=1
                while (r-l+1-count)>k:
                    if s[l]==i:
                        count-=1
                    l+=1
                length=max(r-l+1,length)
                r+=1

        return length



