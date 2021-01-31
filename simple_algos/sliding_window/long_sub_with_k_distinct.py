# Longest subarray with 'k' distinct charecters

def max_subarray_with_k_distinct_char(k, str):
    # create variables
    max_length = 0
    window_start = 0
    char_freq = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        # loop through and create left char/decriument
        while len(char_freq) > k:
            left_char = str[window_start]
            char_freq[left_char] -= 1
            # if char freq of left char = 0 it is not unique.  Remove value
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            # increment window start
            window_start += 1
        # set the max as the greatest of prev max and the length of the current window
        max_length = max(max_length, window_end - window_start + 1)
    # return max window length
    return max_length