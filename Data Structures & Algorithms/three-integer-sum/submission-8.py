class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortlist=sorted(nums)
        res=[]
        hashset={}
        for i in range(len(sortlist)):
            if i>0 and sortlist[i]==sortlist[i-1]:
                continue
            j=i+1
            k=len(sortlist)-1
            while j<k:
                if sortlist[i]+sortlist[j]+sortlist[k]==0 :
                    res.append([sortlist[i],sortlist[j],sortlist[k]])
                    j+=1
                    k-=1
                    while j<k and sortlist[j]==sortlist[j-1]:
                        j+=1
                    while j<k and sortlist[k]==sortlist[k+1]:
                        k-=1
                elif sortlist[i]+sortlist[j]+sortlist[k]>0:
                    k-=1
                elif sortlist[i]+sortlist[j]+sortlist[k]<0:
                    j+=1
        return res
                
