class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int maxCounts=0;
        Map <Integer,Integer> freqCounter =new HashMap<>();
        for (int value:nums){
            freqCounter.merge(value,1,Integer::sum);
            maxCounts=Math.max(maxCounts,freqCounter.get(value));
        }
        List<List<Integer>> bucket = new ArrayList<>();
        for (int i=0;i<=maxCounts;i++){
            bucket.add(new ArrayList<>());
        }
        for (Map.Entry<Integer,Integer> entry:freqCounter.entrySet()){
            bucket.get(entry.getValue()).add(entry.getKey());
        }
        List<Integer> results=new ArrayList<>();
        int counter=0;
        for (int j=maxCounts;j>0;j--){
            for (int i:bucket.get(j)){
                results.add(i);
            }
            counter=counter+bucket.get(j).size();
            if (counter>=k){
                break;
            }

        }
        return results.stream().mapToInt(i->i).toArray();


    }
}
