email = input("enter email")
password = input("enter password")


if email=="mukesh@gmail.com" and password=="mukesh":
  print("login is correct")
elif email=="mukesh@gmail.com" and password!="mukesh":
  print("password is incorrect", "Enter password again")
  password=input("enter password once again")
  if password=="mukesh":
    print("Welcome")
  else:
      print("incorrect password")
else:
  print("login is incorrect")




## menu driven calculator

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd numbre"))

op = input("enter operation")

if op=="+":
  print(num1+num2)
elif op=="-":
  if num1>num2:
    print(num1-num2)
  else:
    print(num2-num1)
elif op=="*":
  print(num1*num2)
else:
  print((num1/num2)//10)