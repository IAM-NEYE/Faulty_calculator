print("what you want to do?")
function=input("+,-,*,/ :")

if function=="+":
  anum1=input("Enter 1st number :")
  anum2=input("Enter 2nd number :")
  if anum1 in ["9","56"] and anum2 in ["9","56"] and anum1!=anum2:
       print(77)
  else:
    print(int(anum1)+int(anum2))

elif function=="-":
  snum1=input("Enter 1st number :")
  snum2=input("Enter 2nd number :")
  print(int(snum1)-int(snum2))

elif function=="*":
  mnum1=input("Enter 1st number :")
  mnum2=input("Enter 2nd number :")
  if mnum1 in ["45","3"] and mnum2 in ["45","3"] and mnum1!=mnum2:
       print(555)
  else:
    print(int(mnum1)*int(mnum2))

elif function=="/":
  dnum1=input("Enter 1st number :")
  dnum2=input("Enter 2nd number :")
  if dnum1 in ["56","6"] and dnum2 in ["56","6"] and dnum1!=dnum2:
       print(4)
  else:
    print(int(dnum1)/int(dnum2))
else:
  print("Enter valid function")
