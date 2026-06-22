class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we can have a sliding window, and expand 
        # we just keep expanding, and then we shrink it to the min one.
        l,r=0,0
        uniquechar=len(set(t))
        res=""
        need={}
        for i in t:
            if i not in need:
                need[i]=1
            else:
                need[i]+=1
        have={}
        for i in need:
            have[i]=0
        satisfied=0
        while r<len(s):
            if s[r] in have:
                have[s[r]]+=1
                if have[s[r]]==need[s[r]]:
                    # need to make sure I dont double satisfy
                    satisfied+=1
            while satisfied==uniquechar:
                if len(res)==0 or len(s[l:r+1])<len(res):
                    res=s[l:r+1]
                if s[l] in have:
                    have[s[l]]-=1
                    if have[s[l]]<need[s[l]]:
                        satisfied-=1
                l+=1
            r+=1
        while satisfied==uniquechar:
                if len(res)==0 or len(s[l:r+1])<len(res):
                    res=s[l:r+1]
                if s[l] in have:
                    have[s[l]]-=1
                    if have[s[l]]<need[s[l]]:
                        satisfied-=1
                l+=1
        return res

