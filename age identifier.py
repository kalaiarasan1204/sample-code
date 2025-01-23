age = int(input("Enter the age:"))

if age >=0 and age <= 12:
  print("Child")
elif age >=13 and age <= 19:
  print("Teenager")
elif age >=20 and age <= 64:
  print("Adult")
elif age >=65:
  print("senior")
else:
  print("age is invalid")
