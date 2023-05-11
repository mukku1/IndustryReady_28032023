n = int(input())
if 1<=n<=100:
    if n%2!=0:
        print("Weird")
    elif n%2==0:
        if n>=2 and n<=5:
            print("Not weird")
        elif n>=6 and n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")
else:
    print("number not in range")