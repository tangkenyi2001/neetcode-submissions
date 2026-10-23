class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> freqCounter=new HashMap<>();
        for (int i=0;i<s.length();i++){
            freqCounter.merge(s.charAt(i),1,(oldvalue,newvalue)->oldvalue+newvalue);
        }
        for (int j=0;j<t.length();j++){
            if (freqCounter.containsKey(t.charAt(j))){
                freqCounter.merge(t.charAt(j),-1,Integer::sum);
            }
            else{
                return false;
            }
        }
        System.out.println(freqCounter);
        for (Map.Entry<Character,Integer> entry:freqCounter.entrySet()){
            if (entry.getValue()!=0){
                return false;
            }
        }
        return true;

    }
}
