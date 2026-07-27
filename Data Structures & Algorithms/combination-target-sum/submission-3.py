
import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #distinct nums:
        # terminating condition is that res=target:
        res=[]
        nums.sort()

        def bt(i,arr):
            if i>=len(nums) or sum(arr)>target:
                return
            if sum(arr)==target:
                res.append(copy.deepcopy(arr))
                return
            arr.append(nums[i])
            bt(i,arr)
            arr.pop()
            bt(i+1,arr)
            

        bt(0,[])

        return res
            
