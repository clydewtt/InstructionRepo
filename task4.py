# This function should return True if the argument is of the int data type

def is_variable_an_integer(var):
    return isinstance(var, str)

assert is_variable_an_integer(10) == True, "10 is an integer, function should return True"

print("Test passed!")