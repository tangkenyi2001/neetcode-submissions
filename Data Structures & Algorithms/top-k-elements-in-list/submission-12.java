class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freqArr = new HashMap<>();
        for (int num : nums){
            freqArr.merge(num,1,Integer::sum);
        }

        List<Integer>[]buckets= new List[nums.length+1];

        for (int i=0;i<nums.length+1;i++){
            buckets[i]= new ArrayList<>();
        }

        for (Map.Entry<Integer,Integer> entry : freqArr.entrySet()){
            buckets[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k]; 
        int count=0;

        for (int j=buckets.length-1;j>0;j--){
            for (int item : buckets[j]){
                res[count++]=item;
                if (count>=k){
                    return res;
                }
            }

        }
        return res;

    }
}
