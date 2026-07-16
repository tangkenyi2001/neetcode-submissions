class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums=sorted(nums)
        i=0
        length=len(nums)
        res=[]
        while i<length:
            j=i+1
            k=length-1
            while j<k:
                if sortedNums[i]+sortedNums[j]+sortedNums[k]==0:
                    res.append([sortedNums[i],sortedNums[j],sortedNums[k]])
                    j+=1
                    while j<length and sortedNums[j]==sortedNums[j-1]:
                        j+=1
                elif sortedNums[i]+sortedNums[j]+sortedNums[k]>0:
                    k-=1
                else:
                    j+=1
            i+=1
            while i<length and sortedNums[i]==sortedNums[i-1]:
                i+=1
        return res