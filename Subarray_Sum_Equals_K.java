class Solution {
    public int subarraySum(int[] nums, int k) {
        /*
        Good Question

        logic:
            - two pointers
            - get sum in slide window between these two pointers
            - if match k, count

        key points:
            - in outer loop reset sum to 0
            - inner loop start from i(outer loop pointer) j=i
            -

        Time  O(N^2)
        Space O(1)

        This algo not works for Python

        */
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            int sum = 0;
            for(int j = i; j < nums.length; j++){
                sum += nums[j];
                if(sum == k){
                    count++;
                }
            }
        }
        return count;
    }

    /*
    Cumulative SUM approach
    */
    public int subarraySum_v2(int[] nums, int k) {
        /*
        "Cumulative SUM"

        Good Example for "Cumulative SUM"

        Logic:
            - create cumulative sum array
            - slide window, sub start and end if match k found

        key points:
            - cumulative sum array length +1 than nums
            - inner loop end at nums length +1, because of sum array is +1 length
        */
        int count = 0;
        int[] sum = new int[nums.length + 1];
        sum[0] = 0;
        for(int i = 1; i < sum.length; i++){
            sum[i] = sum[i - 1] + nums[i - 1];
        }
        // System.out.println(Arrays.toString(sum));
        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length + 1; j++){
                // System.out.println(i);
                // System.out.println(j);
                // System.out.println(sum[j]);
                // System.out.println(sum[i]);
                // System.out.println();
                if((sum[j] - sum[i]) == k){
                    count++;
                }
            }
        }
        return count;
    }
}