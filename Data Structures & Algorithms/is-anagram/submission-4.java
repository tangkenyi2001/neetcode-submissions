class Solution {
    public boolean isAnagram(String s, String t) {
        /*
        1 way is hashmap
        time complex is o(s+t), space is o(26)

        2nd way is an array
        time complex is o(s+t), space is o(26)
        */
        // 
        if (s.length()!=(t.length())){
            return false;
        }
        int[] freqArr=new int[26];
        for (int i=0;i<s.length();i++){
            int index=s.charAt(i)-'a';
            freqArr[index]++;
        }

        for (int i=0;i<t.length();i++){
            int index=t.charAt(i)-'a';
            freqArr[index]--;
        }
        System.out.println(freqArr);
        for (int i=0;i<26;i++){
            if (freqArr[i]!=0){
                return false;
            }
        }
        return true;
    }   
}
