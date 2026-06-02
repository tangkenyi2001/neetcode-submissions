class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[math.inf]*len(coins) for _ in range(amount+1)]
        for i in range(amount+1):
            for j in range(len(coins)):
                #if amount is less than coin
                if i==0:
                    dp[i][j]=0
                #if cannot use current coin
                elif j==0:
                    if i%coins[j]==0:
                        dp[i][j]=i//coins[j]
                elif i-coins[j]<0:
                    dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j]=min(dp[i][j-1],dp[i-coins[j]][j]+1)
        if dp[-1][-1]==math.inf:
            return -1
        else:
            return dp[-1][-1]
