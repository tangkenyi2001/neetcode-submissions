class Solution {
    public boolean hasDuplicate(int[] nums) {
        
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