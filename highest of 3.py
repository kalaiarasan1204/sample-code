# assining values
num1 = 10
num2 = 15
num3 = 25
# writing the comparision function
greatest = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
# printing the ststement
print(f"The Greatest of {num1} , {num2} and {num3} is: {greatest}")
