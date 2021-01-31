# Simple solution for finding the max array of size 'k' in a list

def sliding_window(arr, k):

    result = []
    # create temp sum and start object
    window_sum, window_start = 0.0, 0
    # iterate through each item creating a sliding end value
    for window_end in range(len(arr)):
        # add the last value to the array
        window_sum += arr[window_end]
        # if the end value become equal to the index of the length of the sublist, append, then remove start and increment
        if window_end >= k-1:
            # append the sublist to the result
            result.append(window_sum)
            # remove start value
            window_start -= arr[window_start]
            # increment start value (slide window)
            window_start += 1
    # returns the list of summed windows
    return result

    # can change by returning max(result) or min(result)
    # can also use k to calc the average of the subarrays with result.append(window_sum/k)