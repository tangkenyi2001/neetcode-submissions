class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #maintain a max heap, which maps val:idx
        #each time you move the right window, you add the val:idx into it.
        #at each point of time, we clear the max heap, and remove the max that has a idx lower than left
        maxheap=[ [-1*nums[i],i] for i in range(k)]
        heapq.heapify(maxheap)
        res=[-1*maxheap[0][0]]
        l=1
        r=k
        while r<len(nums):
            heapq.heappush(maxheap,[-1*nums[r],r])
            #remove all those where the idx is less than 1
            while maxheap[0][1]<l:
                heapq.heappop(maxheap)
            res.append(-1*maxheap[0][0])
            l+=1
            r+=1
        return res