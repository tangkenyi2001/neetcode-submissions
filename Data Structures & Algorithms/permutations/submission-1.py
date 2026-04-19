class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        visited=[]
        def bt(i):
            # if it is the same length as the nums
            if len(cur)==len(nums) and cur not in visited:
                res.append(cur[:])
                visited.append(cur[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                cur.append(nums[i])
                bt(i+1)
                cur.pop()
                bt(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        bt(0)
        return res