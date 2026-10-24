class Solution {
    public String longestPalindrome(String s) {
      int longestlength=0;
      String lpalindrome="";
      for (int i=0;i<s.length();i++){
        //two scenarios
        int j=i;
        int k=i;
        while (j>=0 && k<s.length() && s.charAt(j)==s.charAt(k)){
            if ((k-j+1)>longestlength){
                longestlength=k-j+1;
                lpalindrome=s.substring(j,k+1);
            }
            j--;
            k++;
        }
        j=i;
        k=i+1;
        while (j>=0 && k<s.length() && s.charAt(j)==s.charAt(k)){
            if ((k-j+1)>longestlength){
                longestlength=k-j+1;
                lpalindrome=s.substring(j,k+1);
            }
            j--;
            k++;
        }
      }
      return lpalindrome;  
    }
}
