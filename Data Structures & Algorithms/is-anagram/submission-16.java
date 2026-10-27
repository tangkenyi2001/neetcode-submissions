class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freqArr = new int[26];

        if (s.length()!=t.length()){
            return false;
        }

        for (int i=0;i<s.length();i++){
            char curChar = s.charAt(i);
            freqArr[curChar-'a']+=1;
        }

        for (int j=0;j<t.length();j++){
            char curChar = t.charAt(j);
            freqArr[curChar-'a']-=1;
        }
        // for (int i :freqArr){
        //     System.out.println(i);
        // }

        for (int k=0;k<26;k++){
            if (freqArr[k]!=0){
                return false;
            }
        }
        return true;
    }
}
