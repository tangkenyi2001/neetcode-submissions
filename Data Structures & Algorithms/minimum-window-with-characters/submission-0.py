class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we can have a sliding window, and expand 
        # we just keep expanding, and then we shrink it to the min one.
        l,r=0,0
        res=""
        def substring(string1,string2):
            # returns true if string2 is a substring of string1
            hashset={}
            for i in string2:
                if i not in hashset:
                    hashset[i]=1
                else:
                    hashset[i]+=1
            for i in string1:
                if i in hashset:
                    if hashset[i]>0:
                        hashset[i]-=1
            for key,value in hashset.items():
                if value!=0:
                    return False
            return True
        while r<len(s):
            while substring(s[l:r+1],t):
                if len(res)==0 or len(s[l:r+1])<len(res):
                    res=s[l:r+1]
                l+=1
            r+=1
        while substring(s[l:r+1],t):
            if len(res)==0 or len(s[l:r+1])<len(res):
                res=s[l:r+1]
            l+=1
        return res

