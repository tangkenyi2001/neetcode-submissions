class Solution {
    public int characterReplacement(String s, int k) {
        //sliding window, we extend the rhs, and then we contract the left window if its violated
        //window condition basically, ((r-l-mostcommon)<k)
        int l=0;
        char curMaxChar=s.charAt(0);
        Map <Character,Integer> freqCounter=new HashMap<>();
        int longest=0;
        int maxcount=0;
        for (int r=0;r<s.length();r++){
            char curChar=s.charAt(r);
            freqCounter.merge(s.charAt(r),1,Integer::sum);
            if (freqCounter.get(curChar)>freqCounter.get(curMaxChar)){
                curMaxChar=curChar;
            }
            maxcount=Math.max(maxcount,freqCounter.get(curChar));
            while (r-l+1-maxcount>k){
                freqCounter.merge(s.charAt(l),-1,Integer::sum);
                if (freqCounter.get(curChar)>freqCounter.get(s.charAt(l))){
                    curMaxChar=curChar;
                }
                l++;
                //if after deducting it is no longer the max, we need to switch it.
            }
            longest=Math.max(longest,r-l+1);
            
        }
        
        return longest;
        
    }
}
