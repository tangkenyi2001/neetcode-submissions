class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,value in enumerate(nums):
            number2=target-value
            if number2 in hashmap:
                return [hashmap[number2],index]
            else:
                hashmap[value]=index 

