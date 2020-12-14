### Max Sub array Problem
# TWO SOLUTIONS: (merge sort) and the greedy iterative solution
# Runtime: 48 ms (67%)
# Space: 14.1 mb (87%)



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # length of the list
        n = len(nums)
        # set the current and max to the first value in the list
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            # iterate through and check if the next value (v) increases the curr sum
            curr_sum = max(nums[i], curr_sum + nums[i])

            # if the current sum is greater than the max, set max = curr
            max_sum = max(max_sum, curr_sum)


        return max_sum