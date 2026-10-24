
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        List<int[]> res= new ArrayList<>();
        //can have a min heap
        record Item(int distance, int[]point){};
        Queue<Item> heap = new PriorityQueue<>(Comparator.comparingInt(Item::distance));
        for (int[] point : points){
            //sqrt((x1 - x2)^2 + (y1 - y2)^2)
            int distance = point[0] * point[0] + point[1] * point[1];
            heap.offer(new Item(distance,point));
        }
        for (int i=0;i<k;i++){
            Item closestItem=heap.poll();
            res.add(closestItem.point);
        }
        return res.toArray(new int[0][]);


    }
}
