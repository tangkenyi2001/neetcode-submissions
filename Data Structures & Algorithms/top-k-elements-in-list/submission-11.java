class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map <Integer,Integer> freqArray = new HashMap<>();
        for (int num : nums){
            freqArray.merge(num,1,Integer::sum);
        }
        List<Integer>[] bucket = new List[nums.length+1];
        for (int i=0;i<nums.length+1;i++){
            bucket[i]=new ArrayList<Integer>();
        }
        for (Map.Entry<Integer,Integer> entry : freqArray.entrySet()){
            bucket[entry.getValue()].add(entry.getKey());
        }
        int count = 0;
        int[] res = new int[k];
        int index=0;
        for (int j=nums.length;j>=0;j--){
            for (int i : bucket[j]){
                count+=1;
                res[index++]=i;
                if (index>=k){
                    return res;
                }
            }
        }
        return res;

    }
}
