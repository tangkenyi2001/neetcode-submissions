class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #naive approach is to just create a window, and slide along s2, and then each window compute and compare to s1
        s1arr=[0]*26
        s2arr=[0]*26
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            s1idx=ord(s1[i])-ord('a')
            s2idx=ord(s2[i])-ord('a')
            s1arr[s1idx]+=1
            s2arr[s2idx]+=1
        matches=0
        for i in range(26):
            if s1arr[i]==s2arr[i]:
                matches+=1
        # two cases if we remove the element, we check if adding it reduced the match or increased the match
        # two cases if we add the element, we check if adding it reduced the match or increased the match
        for j in range(len(s1),len(s2)):
            if matches==26:
                return True
            # r=3,l=0
            r=j
            l=r-len(s1)

            lidx=ord(s2[l])-ord('a')
            ridx=ord(s2[r])-ord('a')

            s2arr[lidx]-=1
            if s2arr[lidx]==s1arr[lidx]:
                matches+=1
            elif s2arr[lidx]+1==s1arr[lidx]:
                matches-=1
            
            s2arr[ridx]+=1
            if s2arr[ridx]==s1arr[ridx]:
                matches+=1
            elif s2arr[ridx]-1==s1arr[ridx]:
                matches-=1
        return matches==26
            
        