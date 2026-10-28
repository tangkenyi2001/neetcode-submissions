class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> res = new ArrayList<>();
        Arrays.sort(intervals,(a,b)->Integer.compare(a[0],b[0]));
        for (int[] interval : intervals){
            if (res.isEmpty()){
                res.add(interval);
            }
            else if (interval[0]<=res.get(res.size()-1)[1]){
                res.get(res.size()-1)[1]=Math.max(res.get(res.size()-1)[1],interval[1]);
            }
            else{
                res.add(interval);
            }
        }
        //need to map a list to array
        //stream streams out objects
        //need to convert objects to int[]
        return res.stream().toArray(int[][]::new);
    }
}
