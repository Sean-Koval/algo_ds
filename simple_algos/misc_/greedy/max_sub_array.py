### Max Sub array Problem
# TWO SOLUTIONS: (merge sort) and the greedy iterative solution
# Runtime: 48 ms (67%)
# Space: 14.1 mb (87%)


# SOLUTION 1: Greedy
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

# SOLUTION 2: Merge Sort
    class Solution:
        def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   

    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)