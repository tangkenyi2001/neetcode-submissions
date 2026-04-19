class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset={}
        for i in set(nums):
            hashset[i]=1
        start=[]
        for i in hashset.keys():
            if (i-1) not in hashset :
                start.append(i)
        longest=0
        
        for i in start:
            number=i
            cur=1
            while True:
                if (number+1) in hashset:
                    number+=1
                    cur+=1
                else:
                    longest=max(longest,cur)
                    break
        return longest