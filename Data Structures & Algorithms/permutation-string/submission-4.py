class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #naive approach is to just create a window, and slide along s2, and then each window compute and compare to s1
        def counter(string:str):
            hashmap=defaultdict(int)
            for i in string:
                hashmap[i]+=1
            return hashmap
        s1map=counter(s1)
        windowsize=len(s1)
        l=0
        r=windowsize-1
        while r<len(s2):
            print(counter(s2[l:r+1]))
            if counter(s2[l:r+1])==s1map:
                return True
            r+=1
            l+=1
        return False



    

        