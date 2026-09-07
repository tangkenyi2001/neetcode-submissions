class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #naive approach is to just create a window, and slide along s2, and then each window compute and compare to s1
        s2map=defaultdict(int)
        s1map=defaultdict(int)
        for i in s1:
            s1map[i]+=1

        windowsize=len(s1)
        l=0
        r=0

        while r<len(s2) and (r-l)<windowsize:
                s2map[s2[r]]+=1
                r+=1
        if s2map==s1map:
                return True

        while r<len(s2):
            print(s2map)
            print(s1map)
            s2map[s2[r]]+=1
            s2map[s2[l]]-=1
            if s2map[s2[l]]==0:
                del s2map[s2[l]]
            if s2map==s1map:
                return True
            r+=1
            l+=1
        return False



    

        