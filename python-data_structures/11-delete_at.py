def delete_at(my_list=[], idx=0):
    # If idx is negative or out of range, do nothing
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Delete the item at the specified index
    del my_list[idx]
    return my_list
