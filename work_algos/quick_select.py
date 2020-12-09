
# Quick select algo 
def quicj_select(array_list, left, right, k):
    split = partition(array_list, left, right)

    if split == k:
        return split
    elif split < k:
        return quick_select(array_list, split + 1, right, k)
    else:
        return quick_select(array_list, left, split - 1, k)







# This is the partition function that is within quicksort main
def partition(unsorted_list, first_index, last_index, k):
    if first_index == last_index:
        return first_index
    
    pivot = unsorted_list[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    less_than_pivot = index_of_last_element
    greater_than_pivot = first_index + 1

    while True:
        
        while unsorted_list[greater_than_pivot] < pivot and
            greater_than_pivot < last_index:
            greater_than_pivot +=1
        
        while unsorted_list[less_than_pivot] > pivot and
            less_than_pivot > first_index:
            less_than_pivot -= 1
        
        if greater_than_pivot < less_than_pivot:
            temp = unsorted_list[greater_than_pivot]
            unsorted_list[greater_than_pivot] = unsorted_list[less_than_pivot]
            unsorted_list[less_than_pivot] = temp
        else:
            break

    unsorted_list[pivot_index] = unsorted_list[less_than_pivot]
    unsorted_list[less_than_pivot] = pivot
