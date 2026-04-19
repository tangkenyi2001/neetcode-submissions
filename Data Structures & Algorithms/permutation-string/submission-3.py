class Solution:
    def checkInclusion(self,s1: str, s2: str):
        if len(s2)<len(s1):
            return False
        l=0
        r=len(s1)-1
        s1count={}
        s2count={}
        for i in range(len(s1)):
            if s1[i] in s1count:
                s1count[s1[i]]+=1
            else:
                s1count[s1[i]]=1
            if s2[i] in s2count:
                s2count[s2[i]]+=1
            else:
                s2count[s2[i]]=1

        while r<len(s2):
            if s2count==s1count:
                return True
            if s2count[s2[l]]>1:
                s2count[s2[l]]-=1
            else:
                s2count.pop(s2[l])
            l+=1
            r+=1
            if r<len(s2) and s2[r] in s2count:
                s2count[s2[r]]+=1
            elif r<len(s2):
                s2count[s2[r]]=1
        return False
