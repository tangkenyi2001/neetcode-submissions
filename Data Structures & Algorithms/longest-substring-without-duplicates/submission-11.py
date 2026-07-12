class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #maintain a sliding window 
        #naive approach is to for each char, create a string and continue until there is a duplicate in the string
        # time 0n^2, space o(n)

        # use a l,r pointer to maintain the window
        # extend the right pointer, but we must make sure its a substirng from l to r
        #use a dictionary to track last seen of each char
        # each time we see a duplicate, if the last seen is greater than the the left pointer
        l,r=0,0
        hashset={}
        res=0
        while r<len(s):
            if s[r] not in hashset:
                hashset[s[r]]=r
            else:
                if hashset[s[r]]>=l:
                    l=hashset[s[r]]+1
                hashset[s[r]]=r
            res=max(res,r-l+1)
            r+=1
        return res
    

                

