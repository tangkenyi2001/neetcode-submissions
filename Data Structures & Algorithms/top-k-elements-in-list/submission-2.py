class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset={}
        for i in nums:
            if i not in hashset:
                hashset[i]=1
            else:
                hashset[i]+=1
        res=[[] for i in range(len(nums)+1)]
        for i in hashset.keys():
            res[hashset[i]].append(i)
        ans=[]
        j=0
        for i in range(len(nums),-1,-1):
            if j>=k:
                break
            else:
                ans.extend(res[i])
                j+=len(res[i])

        return ans