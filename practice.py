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