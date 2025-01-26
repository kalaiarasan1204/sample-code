# Initial values of the two numbers
a = input("Enter the first number: ")
b = input("Enter the second number: ")

print("Before swapping:")
print("a =", a)
print("b =", b)

# Using a temporary variable to swap
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


