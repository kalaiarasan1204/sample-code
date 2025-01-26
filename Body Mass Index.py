# getting input from the user
KG= float(input("Enter your weight in KG:"))
M = float(input("Enter your height in M:"))
# formula to calculate BMI
BMI = KG/(M*M)
# function for category
if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI < 24.9:
    category = "Normal weight"
elif 25 <= BMI < 29.9:
    category = "Overweight"
else:
    category = "Obesity"
# printing the user input
print("weight:",KG)
print("Height:",M)
# to print the output
print("your BMI is:",BMI)
print("your category is:",category)
