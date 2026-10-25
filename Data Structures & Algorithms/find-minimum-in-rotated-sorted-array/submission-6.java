class Solution {
    public int findMin(int[] nums) {
        int currentMinimum=Integer.MAX_VALUE;
        int l=0;
        int r=nums.length-1;

        while (l<=r){
            int mid = (l+r)/2;
            currentMinimum=Math.min(currentMinimum,nums[mid]);
            if (nums[l]<=nums[r]){
                currentMinimum=Math.min(currentMinimum,nums[l]);
                return currentMinimum;
            }
            else{
                if (nums[mid]>=nums[l]){
                    l=mid+1;
                }
                else{
                    r=mid-1;
                }
            }
        }
        return currentMinimum;
    }
}
