class Solution {
    public String longestPalindrome(String s) {
        int maxlength=0;
        String longestString=s.substring(0,1);
        for (int i=0;i<s.length();i++){
            int j=i;
            int k=i;
            while (0<=j && k<s.length() && s.charAt(j)==s.charAt(k)){
                if (k-j+1>maxlength){
                    maxlength=Math.max(maxlength,k-j+1);
                    longestString=s.substring(j,k+1);
                }
                j--;
                k++;
            }

            j=i;
            k=i+1;
            while (0<=j && k<s.length() && s.charAt(j)==s.charAt(k)){
                if (k-j+1>maxlength){
                    maxlength=Math.max(maxlength,k-j+1);
                    longestString=s.substring(j,k+1);
                }
                j--;
                k++;
            }
        }
        return longestString;
    }
}
