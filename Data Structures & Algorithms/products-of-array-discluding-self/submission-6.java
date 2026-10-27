class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int currentProduct=1;
        for (int i=0;i<nums.length;i++){
            res[i]=currentProduct;
            currentProduct*=nums[i];
        }
        currentProduct=1;
        for (int i=nums.length-1;i>-1;i--){
            res[i]*=currentProduct;
            currentProduct*=nums[i];
        }
        return res;

    }
}  
