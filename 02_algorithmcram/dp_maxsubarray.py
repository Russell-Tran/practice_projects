"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        cache = [0 for i in range(len(nums))]
        cache[0] = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            subarray_sum = nums[i]
            if cache[i-1] > 0:
                subarray_sum += cache[i-1]
            cache[i] = subarray_sum
            best = max(best, cache[i])
        return best