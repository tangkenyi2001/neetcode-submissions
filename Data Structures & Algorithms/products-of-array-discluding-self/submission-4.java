class Solution {
    public int[] productExceptSelf(int[] nums) {
        // First approach is that we can have 2 arrays, one is prefix sum where i index is sum of all lhs until the i index, non inclusive, one is a postfix sum, where 
        int[] prefix = new int[nums.length];
        int[] postfix = new int[nums.length];
        int[] res = new int[nums.length];
        int prefixProduct=1;
        int postfixProduct=1;
        for (int i=0;i<nums.length;i++){
            prefix[i]=prefixProduct;
            prefixProduct=prefixProduct*nums[i];
        }
        for (int j=nums.length-1;j>-1;j--){
            postfix[j]=postfixProduct;
            postfixProduct=postfixProduct*nums[j];
        }

        for (int i=0;i<nums.length;i++){
            res[i]=prefix[i]*postfix[i];
        }
        return res;

    }
}  
