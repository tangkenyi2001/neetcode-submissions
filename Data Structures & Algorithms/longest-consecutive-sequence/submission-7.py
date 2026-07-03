class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=defaultdict(int)
        res=0
        for i in nums:
            if not hashset[i]:
                length=hashset[i-1]+hashset[i+1]+1

                hashset[i+hashset[i+1]]=length
                hashset[i-hashset[i-1]]=length
                hashset[i]=length
                res=max(length,res)
        return res




