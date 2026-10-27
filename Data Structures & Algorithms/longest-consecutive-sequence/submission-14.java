class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> hashset = new HashSet<>();
        for (int num : nums){
            hashset.add(num);
        }
        if (nums.length==0){
            return 0;
        }
        int longestLength=1;
        for (int num : nums){
            if (!hashset.contains(num-1)){
                int cur=num;
                while (hashset.contains(cur+1)){
                    cur++;
                    longestLength=Math.max(longestLength,cur-num+1);
                }
            }
        }
        return longestLength;

    }
}
