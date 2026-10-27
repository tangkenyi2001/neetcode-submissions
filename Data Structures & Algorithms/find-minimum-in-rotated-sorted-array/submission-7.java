class Solution {
    public int findMin(int[] nums) {
        int l=0;
        int r=nums.length-1;

        int minElement=Integer.MAX_VALUE;
        while (l<=r){
            int mid=(l+r)/2;
            minElement=Math.min(minElement,nums[mid]);
            if (nums[r]>=nums[l]){
                minElement=Math.min(minElement,nums[l]);
                return minElement;
            }
            else{
                if (nums[l]<=nums[mid]){
                    l=mid+1;
                }
                else{
                    r=mid-1;
                }
            }
        }
        return minElement;
    }
}
