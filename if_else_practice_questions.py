### 70+ python if else statement important practice questions


                                                        ###     Test 1  ###



# 1. write a program to check whether person is eligible for vote or not 
age = int(input("enter age"))

if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


## 2. to check number entered by user is odd or even

num = int(input("enter number"))

if num%2==0:
    print("even")
else:
    print("odd")


## 3. number is divisible by 7 or not

num = int(input("enter number"))

if num%7==0:
    print("divisible")
else:
    print("not divisible")


## 4. display "Hello" if number entered by user is multiple of 5 otherwise display "Bye"

num = int(input("enter number"))

if num%5==0:
    print("Hello")
else:
    print("Bye")

## 5. calculate electricity bill (accept unit from user) according to following criteria-
#unit : first 100 units - no charge | next 100 units - Rs. 5 per unit  | after 200 units Rs.10 per units

unit = int(input("enter units"))

if unit<=100:
    print("no charge")
elif unit>100 and unit<=200:
    print("Rs. ", (unit-100)*5)
else:
    print("Rs. ", 500+(unit-200)*10)



## display the last digit number

num = int(input("enter number"))

print(num%10)


## last digit of a numer enterd by user is divisible by 3 or not

num = int(input("enter number"))

divisibility = num%10

if divisibility%3==0:
    print("divisible")
else:
    print("not divisible")





                                                                ###     Test 2  ###


## accept percentage from user and display the grade acc to following criteria - 
# marks : >90 - A , >80 and <=90  - B , >=60 and <=80 - C , below 60  - D

percentage = int(input("enter percentage"))

if percentage<60:
    print("D")
elif percentage >=60 and percentage<=80:
    print("C")
elif percentage>80 and percentage<=90:
    print("B")
else:
    print("A")




##  accept the cost price of bike and display the road tax to be paid acc to following criteria
# costprice : >1000000 - 15% | >50000 and <=1000000 - 10%    |   <=50000  - 5%

costprice = int(input("enter costprice"))

if costprice<=50000:
    print(0.05*costprice)
elif costprice>50000 and costprice<=100000:
    print(0.1*costprice)
else:
    print(costprice*0.15)



## check whether a year is leap year or not entered by user

year = int(input("enter year"))

if year%4==0:
    print("Leap year")
else:
    print("Not a Leap year")



## accept number from user from 1 to 7 and display the name of the day like 1 for sunday , 2 for monday and so on.

num1 = int(input("enter number"))

if num1==1 :
    print("Sunday")
elif num1==2 :
    print("Monday")
elif num1==3 :
    print("Tuesday")
elif num1==4 :
    print("Wednesday")
elif num1==5 :
    print("Thursday")
elif num1==6 :
    print("Friday")
elif num1==7 :
    print("Saturday")
else:
    print("enter number between 1 to 7")




## accept number from 1 to 12 and display name of the month and days in that month like 1 for january and number of days 31 and so on.

num = int(input("enter num"))

if num==1:
    print("January - 31 days")
elif num==2:
    print("February - 28 days")
elif num==3:
    print("March - 31 dayss")
elif num==4:
    print("April - 30 days")
elif num==5:
    print("May - 31 days")
elif num==6:
    print("June - 30 days")
elif num==7:
    print("July - 31 days")
elif num==8:
    print("August - 31 days")
elif num==9:
    print("September - 30 days")
elif num==10:
    print("October - 31 dayss")
elif num==11:
    print("November - 30 days")
elif num==12:
    print("December - 31 days")

else:
    print("enter number between 1 to 12")




## what do you mean by statement ?
# Executable lines in a program is called instruction/statement.

## write logical expression for the following:
# A is greater than B and C is greater than D

A = int(input("enter any number"))
B = int(input("enter any number"))
C = int(input("enter any number"))
D = int(input("enter any number"))

if A>B and C>D:
    print("sahi hai beta")
else:
    print("tosa na ho payga beta")




## accept any city  from the user and display monument of that city 

city = input("enter city")

if city=="Delhi":
    print("Red fort")
elif city=="Agra":
    print("Tajmahal")
elif city=="Jaipur":
    print("Jal mahal")

else:
    print("enter city from the required list")



## check whether a entered number is 3 digit or not

num = input("enter number")

l = len(num)

if l!=3:
    print("wrong number")
else:
    print("3 digit number")




## check person is eligible for voting or not 

age = int(input("enter your age"))

if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")





##check whether the person is senior citizen or not 

age = int(input("enter your age"))

if age>=60:
    print("you are senior citizen")
else:
    print("you are not senior citizen")



## find the lowest number out of 2 numbers accepted from user

num1 = int(input("enter num 1"))
num2 = int(input("enter num 2"))

if num1>num2:
    print(num2)
else:
    print(num1)



## whether a number accepted by user is divisible by 2 and 3 both

num = int(input("enter number"))

if num%2==0 and num%3==0:
    print("divisible by 2 and 3 both")
else:
    print("not divisible")



## prime number or not

num = int(input("enter number"))

i=2
for i in range(2,num):
  if num%i==0:
    print("number is not prime")
    i+=1
    break
else:
  print("number is prime")



## accept the number from the user and calculate the percentage and display eligibility for more than 75%

working_days = int(input("enter total working days"))
absent_days = int(input("enter total absent days"))

class_attended = (working_days/(working_days+absent_days))*100

class_attended_rate=format(class_attended,".2f")
print(class_attended_rate)
if class_attended>=75:
  print("you are eligible to sit in exam")
else:
  print("you are not eligibel to sit in exam")




## accept the age ,sex(M,F),number of days and display the wages accordingly

age = int(input("enter age"))
sex = input("enter sex")
if age>=18 and age<30:
    if sex=="M":
        print("700 per day")
    elif sex=="F":
        print("750 per day")
    else:
        print("enter correct sex")
elif age>=30 and age<=40:
    if sex=="M":
        print("800 per day")
    elif sex=="F":
        print("850 per day")
    else:
        print("enter correct sex")
else:
    print("enter age between 18 and 40")