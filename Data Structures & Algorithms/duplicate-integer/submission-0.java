class Solution {
    public boolean hasDuplicate(int[] nums) {
        /*
        1 way, we have a set, each time we see a new item, we check the set first before putting it in, if it is in the set, we return false, time o(n) space o(n)
        */
        Map<Integer,Boolean> freqCounter=new HashMap<>();

        for (int i=0;i<nums.length;i++){
            if (freqCounter.containsKey(nums[i])){
                return true;
            }
            else{
                freqCounter.put(nums[i],true);
            }
        }
        return false;
    }
}