# This function should return True if the argument is a positive number

def is_number_positive(num):
    return num < 0

assert is_number_positive(-40) == False, "-40 is negative, function should return False"

print("Tests passed!")