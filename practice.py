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




import math
math.factorial(5)



import keyword

keyword.kwlist   ### '''['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']'''


import random
print(random.randint(1,10))


import datetime
print(datetime.datetime.now())





num = int(input("enter number"))

i = 1

while i<=10:
  print(num," x ",i," ", "=" ,num*i )
  i+=1





import random
jackpot=random.randint(1,100)
guess = int(input("enter number"))

counter=1
while guess!=jackpot:
  if guess<jackpot:
    print("guess higher")
  else:
    print("guess lower")
  guess = int(input("enter number"))
  counter+=1
print("correct guess")
print("gussed in ", counter,"th", "attempt")





for i in range(1,11):
  if i<=5:
    print(i)
  else:
    print(i+100)






for i in range(1,11,2):
  print(i)





for i in [1,2,3,4,5]:
  x=print(i)
  print(x)





curr_pop=10000

for i in range(10,0,-1):
  print(i, curr_pop)
  curr_pop=curr_pop+0.1*curr_pop



curr_pop=10000

for i in range(10,0):
  curr_pop=curr_pop/1.1
  print(i, curr_pop)
  




