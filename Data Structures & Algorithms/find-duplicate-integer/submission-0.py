class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyds algo

        fast,slow=0,0
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if fast==slow:
                break
        secondslow=0
        while True:
            slow=nums[slow]
            secondslow=nums[secondslow]
            if slow==secondslow:
                return slow
