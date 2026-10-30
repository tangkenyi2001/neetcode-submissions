class Solution {
    List <List<Integer>> res;
    List <Integer> path;
    int[] nums;
    private void bt(int index,int curSum, int target){
        if (curSum==target){
            res.add(List.copyOf(path));
            return;
        }
        else if (curSum>target){
            return;
        }
        for (int i=index;i<nums.length;i++){
            path.add(nums[i]);
            bt(i,curSum+nums[i],target);
            path.remove(path.size()-1);
        }

        
    }
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        this.res = new ArrayList<>();
        this.nums = nums;
        this.path = new ArrayList<>();
        bt(0,0,target);
        return this.res;


    }
}
