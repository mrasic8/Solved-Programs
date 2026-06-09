import java.util.HashSet;
class Solution{
    public int[] intersection(int[] nums1, int[] nums2) {
        Hashset<Integer> seen=new Hashset<>();
        Hashset<Integer> intersect=new Hashset<>();
        for(int num:nums1){
            seen.add(num);
        }
        for(int num:nums2){
            if(seen.contains(num)){
                intersect.add(num);
            }
        }
        int result[]=new int[intersect.size()];
        int index=0;
        for(int num:intersect){
            result[index++]=num;
        }
        return result;
    }
}


