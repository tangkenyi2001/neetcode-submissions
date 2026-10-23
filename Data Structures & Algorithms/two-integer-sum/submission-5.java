class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map <Integer,Integer> hashmap =new HashMap<>();

        for (int i=0;i<nums.length;i++){
            int need=target-nums[i];
            if (hashmap.containsKey(need)){
                int[] result={hashmap.get(need),i};
                return result;
            }
            else{
                hashmap.put(nums[i],i);
            }
        }
        return new int[2];
    }
}
