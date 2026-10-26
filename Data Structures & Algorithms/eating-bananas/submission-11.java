class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int upperbound = Arrays.stream(piles).max().getAsInt();
        int lowerbound=1;
        // int minEatingSpeed = Integer.MAX_VALUE;
        int res = upperbound;
        while (lowerbound<=upperbound){
            int mid=(upperbound+lowerbound)/2;
            int hours=0;
            for (int i : piles){
                hours+=Math.ceil((double)i/mid);
            }
            if (hours<=h){
                res=mid;
                upperbound=mid-1;
            }
            else{
                lowerbound=mid+1;
            }

        }
        return res;
    }
}
