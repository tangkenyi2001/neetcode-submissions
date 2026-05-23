class Solution:
    def intToBinary(self,n: int)->int:
        res=0
        cur=n
        count=0
        while (cur/2)>0:
            remainder=n%2
            cur=cur//2
            res+=remainder*pow(10,count)
            count+=1
        return res
    def countBits(self, n: int) -> List[int]:
        #if its odd, it will be just one different from the one above
        #if its even it will be the same as half of it.
        #need to set inital case, which is 0 and 1,
        dp=[0 for _ in range(n+1)]
        # need to consider basecase
        if n==0:
            return [0]
        elif n==1:
            return [0,1]
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            if i%2==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=dp[i-1]+1
        return dp
        
