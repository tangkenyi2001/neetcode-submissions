class Solution {
    public int longestConsecutive(int[] nums) {
        Map <Integer,Integer> hashmap = new HashMap<>();
        if (nums.length<=1){
            return nums.length;
        }

        int longest=1;
        int leftLength;
        int rightLength;
        int newlength;
        for (int i:nums){
            if (hashmap.containsKey(i)){
                continue;
            }
            else{
                if (hashmap.containsKey(i-1) && hashmap.containsKey(i+1)){
                    leftLength=hashmap.get(i-1);
                    rightLength=hashmap.get(i+1);
                    newlength=leftLength+rightLength+1;
                    longest=Math.max(longest,newlength);
                    hashmap.put(i-hashmap.get(i-1),newlength);
                    hashmap.put(i+hashmap.get(i+1),newlength);
                    hashmap.put(i,newlength);

                }
                else if (hashmap.containsKey(i-1)){
                    leftLength=hashmap.get(i-1);
                    newlength=leftLength+1;
                    longest=Math.max(longest,newlength);
                    hashmap.put(i-hashmap.get(i-1),newlength);
                    hashmap.put(i,newlength);
                }
                else if (hashmap.containsKey(i+1)){
                    rightLength=hashmap.get(i+1);
                    newlength=rightLength+1;
                    longest=Math.max(longest,newlength);
                    hashmap.put(i+hashmap.get(i+1),newlength);
                    hashmap.put(i,newlength);
                }
                else{
                    hashmap.put(i,1);
                }
            }
        }
        System.out.println(hashmap);
        return longest;
    }
}
