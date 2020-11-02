### This function returns index position for element




def searching(search_arr, x):
    for i in range(len(search_arr)):
        if search_arr == x:
            return i
    return -1