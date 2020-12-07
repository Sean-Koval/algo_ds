# This is a function that is faster than a binary search

def nearest_mid(input_list, first, end, search_value):
    return first + ((end - first) //(input_list[end] - input_list[first])) * (search_value  - input_list[first])




def interpolation_search(ordered_list, term):
    size_of_list = len(ordered_list) - 1

    first = 0
    last_element = size_of_list

    while first <= last_element:
        mid = nearest_mid(ordered_list, first, last_element, term)

        if mid > first or mid < first:
            return None
        
        if term > ordered_list[mid]:
            first = mid + 1
        else:
            last_element = mid - 1
    
    if first > last_element:
        return None


