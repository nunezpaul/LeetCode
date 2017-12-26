'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        if (numbers.length < 1){
            return null;
        }
        
        int[] ans = new int[2];
        
        Map<Integer, Integer> seen = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < (numbers.length); i++) {
            
            if (seen.containsKey(target - numbers[i])) {
                ans[0] = seen.get(target - numbers[i])+1;
                ans[1] = i + 1;
            }
            seen.put(numbers[i],i);
        }
    return ans;
    }
}
