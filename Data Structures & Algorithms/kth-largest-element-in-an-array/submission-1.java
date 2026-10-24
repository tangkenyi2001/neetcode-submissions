class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer>queue=new PriorityQueue<>(Comparator.reverseOrder());

        for (int num : nums){
            queue.offer(num);
        }
        int counter=0;
        while (queue.size()>0){
            int removedValue=queue.poll();
            counter++;
            if (counter==k){
                return removedValue;
            }
        }
        return 0;
    }
}
