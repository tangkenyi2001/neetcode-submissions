class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #naive approach iterate through nums, then map to a dictionary, and then put all of them into a heap and heapify
        #o(n) space, o(n) time

        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        heap=[]
        heapq.heapify(heap)
        for key,value in hashmap.items():
            heapq.heappush(heap,[-1*value,key])
        res=[]
        for i in range(k):
            value,key=heapq.heappop(heap)
            res.append(key)
        return res