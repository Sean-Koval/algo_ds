# The negative x has to the do with the fact that heapq is a min heap
def move_val(h1, h2):
    x, i = heapq.heappop(h1)
    heapq.heappush(h2, (-x, i))

# calculates the median of the given heaps (pulling top value and if even dividing)
def get_med(h1, h2, k):
    return h2[0][0] * 1.0 if k & 1 else (h2[0][0] - h1[0][0]) / 2.0


class Solution(object):


    # The negative x has to the do with the fact that heapq is a min heap
    def move_val(h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))

    # calculates the median of the given heaps (pulling top value and if even dividing)
    def get_med(h1, h2, k):
        return h2[0][0] * 1.0 if k & 1 else (h2[0][0] - h1[0][0]) / 2.0

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        # create the two heaps
        small, large = [], []

        for i, x in enumerate(nums[:k]):
            heapq.heappush(small, (-x, i))

        for _ in range(k-(k>>1)):
            move_val(small, large)

        # median for the window
        ans = [get_med(small, large, k)]

        # loop through and place the values in large / small
        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i] <= large[0][0]:
                    move_val(large, small)

            else:
                heapq.heappush(small, (-x, (i + k)))
                if nums[i] >= large[0][0]:
                    move_val(small, large)

            while small and small[0][1] <= i:
                heapq.heappop(small)

            while large and large[0][1] <= i:
                heapq.heappop(large)

            # calc med and append to ans
            ans.append(get_med(small, large, k))


        return ans