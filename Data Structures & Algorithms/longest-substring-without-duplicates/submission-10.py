class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        hashmap={}
        longestsub=0
        for r in range(len(s)):
            if s[r] in hashmap:
                l=max(l,hashmap[s[r]]+1)
                hashmap[s[r]]=r
            else:
                hashmap[s[r]]=r
            longestsub=max(longestsub,(r-l)+1)
        return longestsub
            
            
