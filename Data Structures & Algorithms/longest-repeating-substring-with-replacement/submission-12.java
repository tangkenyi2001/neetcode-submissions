class Solution {
    public int characterReplacement(String s, int k) {
        Map <Character,Integer> hashmap = new HashMap<>();
        int r=0;
        int l=0;
        int maxf=0;
        int res =0;
        while (r<s.length()){
            hashmap.merge(s.charAt(r),1,Integer::sum);
            if (hashmap.get(s.charAt(r))>maxf){
                maxf=hashmap.get(s.charAt(r));
            }
            System.out.printf("r--%d%n",r);
            while (r-l+1-maxf>k){
                System.out.printf("l--%d%n",l);
                hashmap.merge(s.charAt(l),-1,Integer::sum);
                l++;
            }
            res=Math.max(res,r-l+1);
            r++;

        }
        return res;
    }
}
