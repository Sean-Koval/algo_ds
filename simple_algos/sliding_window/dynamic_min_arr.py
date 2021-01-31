import math

def min_array_with_sum(s, arr):

    window_sum = 0.0
    window_start = 0
    min_window = math.inf

    for window_end in range(0, len(arr)):
        # increase the window_sum
        window_sum += arr[window_end]
        # whenever the sum >= to the passed value we set the window and slide window
        while window_sum >= s:
            # set the min window as the smallest of the prev min or the new window size
            min_window = min(min_window, window_end - window_start - 1)
            # reduce the sum by the start
            window_sum -= arr[window_start]
            # slide the window start by one
            window_start += 1
    # return 0 if the min window was never found
    if min_window == math.inf:
        return 0
    # return min window
    return min_window