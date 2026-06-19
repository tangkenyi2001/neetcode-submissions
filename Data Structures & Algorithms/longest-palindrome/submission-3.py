class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=0
        hashset={}
        for i in s:
            if i not in hashset:
                hashset[i]=1
            else:
                hashset[i]+=1
        flag=False
        for key,value in hashset.items():
            #if its even we can add it 
            # if its odd we take the longest odd
            if value%2==0:
                res+=value
            else:
                flag=True
                res+=value-1
        if res==0:
            return 1
        return res+1 if flag else res
