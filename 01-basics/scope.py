# Scope in Python
#x = 20
def new():
    # This function demonstrates the concept of scope in Python
    global x  # Declare x as global to modify the global variable
    x = 10
    print("Inside new(): x =", x)  # Accessing variable
new()
print("Outside new(): x =", x)  # Accessing variable