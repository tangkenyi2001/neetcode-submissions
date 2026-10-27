class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> hashmap = new HashMap<>();
        int maxlength=0;
        int l=0;
        int r=0;
        while (r<s.length()){
            char curChar=s.charAt(r);
            if (!hashmap.containsKey(curChar)){
                hashmap.put(curChar,r);
            }
            else{
                int lastSeen=hashmap.get(curChar);
                l=Math.max(lastSeen+1,l);
                hashmap.put(curChar,r);
            }
            maxlength=Math.max(maxlength,r-l+1);
            r++;
        }

        return maxlength;
    }
}
