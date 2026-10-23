class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int i=0;
        int j;
        int k;
        int curSum;
        List<List<Integer>> result= new ArrayList<>();

        while (i<nums.length-2){
            j=i+1;
            k=nums.length-1;
            while (j<k){
                curSum=nums[i]+nums[j]+nums[k];
                if (curSum==0){
                    result.add(Arrays.asList(nums[i],nums[j],nums[k]));
                    j++;
                    while (j<k && nums[j]==nums[j-1]){
                        j++;
                    }
                    k--;
                }
                else if (curSum>0){
                    //move right
                    k--;
                }
                else if (curSum<0){
                    //move left
                    j++;
                }
            }
            i++;
            while (i<nums.length && nums[i]==nums[i-1]){
                i++;
            }
        }
        return result;

    }
}
