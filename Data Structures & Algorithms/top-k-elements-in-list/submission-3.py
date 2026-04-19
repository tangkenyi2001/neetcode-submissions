class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for _ in range(len(nums)+1)]
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        for key,value in hashmap.items():
            buckets[value].append(key)
        res=[]
        for bucket in range(len(buckets)-1,-1,-1):
            res.extend(buckets[bucket])
            if len(res)==k:
                return res


