print("What is your age?")
age1=int(input())
if 5>age1 or age1>100:
  print("Enter an sensible age!")
elif age1>18:
  print("You can drive the car.")
elif age1==18:
  print("We can't decide,you need to come here and give a test")
else:
  print("Kid! You can't drive a car!")