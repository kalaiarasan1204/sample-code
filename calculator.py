# function to calculate
def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide  (x,y):
  if y == 0:
    return "Error! Division by zero"
  return x / y
# to print the option to user
print("select option:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
# to get the input
choice = input("Enter the choice(1/2/3/4/5):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
# to perform choosem operation
if choice == '1':
   print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
   print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
   print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
   print(f"{num1} / {num2} = {divide(num1, num2)}")
elif choice == '5':
   print(f"{num1} % {num2} = {divide(num1, num2)}")
else:
   print("Invalid Input")
