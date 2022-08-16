class Solution {
    public boolean isMonotonic(int[] nums) {
        int store = 0;
        for(int i = 0; i < nums.length - 1; ++i) {
            int c = Integer.compare(nums[i], nums[i + 1]);
            if(c != 0) {
                if(c != store && store != 0) {
                    return false;
                }
                store = c;
            }
        }
        return true;
    }
}
