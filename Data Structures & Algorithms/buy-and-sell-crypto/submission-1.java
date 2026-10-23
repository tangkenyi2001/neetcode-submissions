class Solution {
    public int maxProfit(int[] prices) {
        //should have running count on min u see
        int minPrice=101;
        int maxProfit=0;
        for (int price : prices){
            if (price<minPrice){
                minPrice=price;
            }
            maxProfit=Math.max(maxProfit,price-minPrice);
        }
        return maxProfit;
        
        
    }
}
