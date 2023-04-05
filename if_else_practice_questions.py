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



