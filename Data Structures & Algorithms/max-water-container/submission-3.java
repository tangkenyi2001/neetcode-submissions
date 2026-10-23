class Solution {
    public int maxArea(int[] heights) {
        //so at any point of time, the max water the container can store is the min(left,right)*(r-l+1), so if we want to maximize it, we always move the smaller one inwards
        int l=0;
        int r=heights.length-1;
        int maxheight=0;
        int curWater;
        while (l<r){
            curWater=Math.min(heights[l],heights[r])*(r-l);
            maxheight=Math.max(maxheight,curWater);
            if (heights[l]>heights[r]){
                r--;
            }
            else{
                l++;
            }
        }
        return maxheight;

    }
}
