num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
# using loop statement to find larger number
if num1 > num2:
  larger = num1
elif num2 > num1:
  larger = num2
else:
  larger = None
# print the values
if larger is None:
  print("Both the numbers are equal")
else:
  print(f"the larger number between {num1} and {num2} is {larger}")
