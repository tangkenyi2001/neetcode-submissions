class Solution {
    public int[][] kClosest(int[][] points, int k) {
        record Point (int[] point, double distance){};
        Queue <Point> minheap = new PriorityQueue<>(Comparator.comparing(Point::distance));
        for (int[] point : points){
            double distance = Math.sqrt((point[0])*(point[0]) + (point[1])*(point[1]));
            minheap.offer(new Point(point,distance));
        }
        int[][] res = new int[k][2];
        for (int i=0;i<k;i++){
            Point curPoint = minheap.poll();
            res[i][0] = curPoint.point()[0];
            res[i][1] = curPoint.point()[1];
        }
        return res;

    }
}
