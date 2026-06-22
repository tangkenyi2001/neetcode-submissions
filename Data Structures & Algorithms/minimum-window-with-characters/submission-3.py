class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we can have a sliding window, and expand 
        # we just keep expanding, and then we shrink it to the min one.
        l,r=0,0
        uniquechar=len(set(t))
        resl,resr=0,0
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
        reslen=math.inf
        while r<len(s):
            if s[r] in have:
                have[s[r]]+=1
                if have[s[r]]==need[s[r]]:
                    # need to make sure I dont double satisfy
                    satisfied+=1
            while satisfied==uniquechar:
                if (r-l+1)<reslen:
                    reslen=r-l+1
                    resr=r
                    resl=l
                if s[l] in have:
                    have[s[l]]-=1
                    if have[s[l]]<need[s[l]]:
                        satisfied-=1
                l+=1
            r+=1
        
        return s[resl:resr+1] if reslen!=math.inf else ""

