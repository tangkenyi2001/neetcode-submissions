class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap={}
        longest=0

        for num in nums:
            if num in hashmap:
                continue
            elif num-1 in hashmap and num+1 in hashmap:
                length=hashmap[num+1]+hashmap[num-1]+1
                hashmap[num-hashmap[num-1]]=length
                hashmap[num+hashmap[num+1]]=length
            elif num-1 in hashmap:
                length=hashmap[num-1]+1
                hashmap[num-hashmap[num-1]]=length
            elif num+1 in hashmap:
                length=hashmap[num+1]+1
                hashmap[num+hashmap[num+1]]=length
            else:
                length=1

            hashmap[num]=length
            longest=max(longest,length)
        return longest

            

