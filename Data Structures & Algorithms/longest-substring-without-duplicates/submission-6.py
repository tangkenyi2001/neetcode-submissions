class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset={}
        #keep track of characters in the string,if it already exists,
        #replace it with the new index and move the start of the string to after the old index
        length=0
        l=0
        r=0
        while r<len(s):
            if s[r] not in hashset:
                #add it to hashset
                hashset[s[r]]=r

            else:
                if hashset[s[r]]>=l:
                    l=hashset[s[r]]+1
                hashset[s[r]]=r
            length=max(length,r-l+1)
            r+=1
        return length