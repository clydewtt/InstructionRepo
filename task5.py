# This function should return True if the argument's list size is 5

def is_list_length_5(lst):
    return len(lst) == 5

assert is_list_length_5([1,2,3,4,5]) == True, "The length of the list is 5, function should return True"

print("Test passed!")