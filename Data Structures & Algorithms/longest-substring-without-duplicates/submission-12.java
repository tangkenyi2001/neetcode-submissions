class Solution {
    public int lengthOfLongestSubstring(String s) {
        // we want a sliding window, so each time we add a new char into the window, we move to left pointer until the current one is valid.
        Map <Character,Integer> lastSeen = new HashMap<>();
        int l=0;
        int maxlength=0;
        for (int r=0;r<s.length();r++){
            char cur =s.charAt(r);
            if (lastSeen.containsKey(cur)){
                //need to shift after the last seen but cannot shift before the l
                l=Math.max(lastSeen.get(cur)+1,l);
                lastSeen.put(cur,r);
            }
            else{
                lastSeen.put(cur,r);
            }
            maxlength=Math.max(maxlength,r-l+1);
        }
        return maxlength;
    }
}
