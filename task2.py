# This function should return whether or not the argument is greater than 100

def is_age_greater_than_100(age):
    return age < 100

assert is_age_greater_than_100(25) == False, "25 is less than 100, function should return False"

print("Test passed!")