# basicall same as quick selection 
# seraches for approx meadian of medians instead of using the first element

def partition(unsorted_arrray, first_index, last_index):

    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_median(unsorted_arrray[first_index:last_index])
        index_of_nearest_median = get_index_of_nearest_median(unsorted_arrray ,first_index,
                                                      last_index, nearest_median)
        
        swap(unsorted_arrray, first_index, index_of_nearest_median)

        pivot = unsorted_arrray[first_index]
        index_of_last_element = last_index

        less_than_pivot_index = index_of_last_element
        greater_than_pivot = first_index + 1




# Median of median methods

def median_of_median(elems):
    # this will create 5 sublists
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)]

    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublists)//2])
    
    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_median(medians)


# get the index of the approximate median

def get_index_of_nearest_median(array_list, first, second, median):
    if first == second:
        return first
    else:
        return first + array_list[first:second].index(median)

def swap(array_list, first, second):
    temp = array_list[first]
    array_list[first] = array_list[second]
    array_list[second] = temp




