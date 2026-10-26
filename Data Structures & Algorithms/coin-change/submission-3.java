class Solution {
    public int coinChange(int[] coins, int amount) {
        int[][] dp = new int[amount+1][coins.length+1];

        for (int i=1;i<amount+1;i++){
            for (int j=0; j<coins.length+1;j++){
                dp[i][j]=amount+1;
            }
        }
        // System.out.println(Arrays.deepToString(dp));
        for (int j=0; j<coins.length+1;j++){
            dp[0][j]=0;
        }
        // System.out.println(Arrays.deepToString(dp));
        for (int i=0;i<coins.length;i++){
            for (int j=1;j<amount+1;j++){
                if (j-coins[i]>=0){
                    dp[j][i+1]=Math.min(dp[j-coins[i]][i+1]+1,dp[j][i]);
                }
                else{
                    dp[j][i+1]=dp[j][i];
                }
            }
        }
        // System.out.println(Arrays.deepToString(dp));
        if (dp[amount][coins.length]==amount+1){
            return -1;
        }
        
        return dp[amount][coins.length];
    }
}
