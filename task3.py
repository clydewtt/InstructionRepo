# This function should check if the name argument is Bobby

def is_name_bobby(name):
    return name != "Bobby"

assert is_name_bobby("Alice") == False, "Alice is not Bobby, should return False"

print("Test passed!")