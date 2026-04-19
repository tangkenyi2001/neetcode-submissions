class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset={}
        for i in nums:
            hashset[i]=1
        start=[]
        for i in nums:
            if i-1 not in hashset:
                start.append(i)
        longest=0
        for i in start:
            curlength=1
            cur=i
            while cur+1 in hashset:
                cur+=1
                curlength+=1
            longest=max(longest,curlength)
        return longest