class Solution {
    public int findMin(int[] nums) {
        int l=0;
        int r=nums.length-1;
        int mid;
        int minVal=nums[0];
        while (l<=r){
            if (nums[r]>nums[l]){
                minVal=Math.min(minVal,nums[l]);
                return minVal;
            }
            mid=(l+r)/2;
            minVal=Math.min(minVal,nums[mid]);
            if (nums[mid]>=nums[l]){
                l=mid+1;
            }
            else{
                r=mid-1;
            }

        }
        return minVal;
    }
}
