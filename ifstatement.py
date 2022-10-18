# 17. Write a program to check whether a person is eligible for voting or not.
age = int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# 18. Write a program to check whether the number entered by the user is even or odd.
num = int(input("enter any number:"))
if num%2==0:
    print("even")
else:
    print("odd")

# 19. Write a program to check whether a number is divisible by 7 or not.
v1= int(input("enter any number:"))
if v1%7==0:
    print("it is divisible by 7")
else:
    print("it is not divisible by 7")

# 20. Write a program to display "Hello" if a number entered by the user is a multiple of five, otherwise print "Bye".
v1 = int(input("enter any number:"))
if v1%5==0:
    print("Hello")
else:
    print("Bye")

# 21. Write a program to display the last digit of a number.
num2 = int(input("enter any number:"))
print(num2%10)

# 22. Write a program to check whether the last digit of a number is divisible by 3 or not.
num1 = int(input("enter any number:"))
num2 = num1%10
if num2%3==0:
    print("the last digit is divisible by 3")
else:
    print("the last digit is not divisible by 3")

# 23. Write a program to check whether a year is a leap year or not.
num4 = int(input("enter a year:"))
if num4%4 == 0 and num4%100 == 0 or num4%400==0:
    print("leap year")
else:
    print("not a leap year")

# 24. Write a program to check if a given number is a Fibonacci number?

# 25. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 7 for Saturday.
day = int(input("enter any number(1-7):"))
if (day == 1):
     print("sunday")
if (day == 2):
     print("monday")
if (day == 3):
     print("tuesday")
if (day == 4):
     print("wednesday")
if (day == 5):
     print("thursday")
if (day == 6):
     print("friday")
if (day == 7):
     print("saturday")
if (day <= 0):
     print("others")
if (day >= 8):
     print("others")

# 26. Write a program to accept a number from 1 to 12 and display the name of the month and days in that month like 1 for Jan and number of days 31 and so on.
if (num == 1):
    print("january")
    print("number of days=31")
if (num==2):
    print("february")
    print("number of days=30")
if (num==3):
    print("march")
    print("number of days=31")
if (num==4):
    print("april")
    print("number of days=30")
if (num==5):
    print("may")
    print("number of days=31")
if (num==6):
    print("june")
    print("number of days=30")
if (num==7):
    print("july")
    print("number of days=31")
if (num==8):
    print("august")
    print("number of days=31")
if (num==9):
    print("september")
    print("number of days=30")
if (num==10):
    print("october")
    print("number of days=31")
if (num==11):
    print("november")
    print("number of days=30")
if (num==12):
    print("december")
    print("number of days=31")
if (num<1):
    print("out of range")
if (num>12):
    print("out of range")

# 27. Write a program which accepts district names from the user and print the central city of that district.

# 28. Write a program to check whether a person is a senior citizen or not.
age = int(input("enter your age:"))
if age>=60:
    print("senior citizen")
else:
    print("not senior citizen")

# 29. Write a program to find the largest number out of two numbers input by the user.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1>num2:
    print("the largest number is:",num1)
else:
    print("the largest number is:",num2)

# 30. Write a program to find the largest number out of three numbers input by the user.
first= int(input("enter first number:"))
second= int(input("enter second number:"))
third= int(input("enter third number:"))
if first>second and first>third:
    print("the largest number is:",first)
elif second>first and second>third:
    print("the largest number is:",second)
else:
    print("the largest number is:",third)

# 31. Write a program to find the lowest number out of two numbers input by the user.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1<num2:
     print("the lowest number is:",num1)
else:
     print("the lowest number is:",num2)

# 32.  Write a program to find the lowest number out of three numbers input by the user.
v1= int(input("enter fisrt number:"))
v2= int(input("enter second number:"))
v3= int(input("enter third number:"))
if v1<v2 and v1<v3:
    print("the lowest number is:",v1)
elif v2<v1 and v2<v3:
    print("the lowest number is:",v2)
else:
    print("the lowest number is:",v3)

# 33. Write a program to find the second largest number out of three numbers by the user.
v1= int(input("enter fisrt number:"))
v2= int(input("enter second number:"))
v3= int(input("enter third number:"))
if v1>v2 and v1<v3:
    print("the  second largest number is:",v1)
elif v2>v1 and v2<v3:
    print("the  second largest number is:",v2)
else:
    print("the second largest number is:",v3)

# 34. Write a program to find the second lowest number out of three numbers input by the user.
v1= int(input("enter fisrt number:"))
v2= int(input("enter second number:"))
v3= int(input("enter third number:"))
if v1>v2 and v1<v3:
    print("the  second lowest number is:",v1)
elif v2>v1 and v2<v3:
    print("the  second lowest is:",v2)
else:
    print("the  second lowest number is:",v3)

# 35. Write a program to check whether a number is even or odd.
num1 = int(2)
if num1%2==0:
    print("even")
else:
    print("odd")

# 36. Write a program to check whether a number (accepted from the user) is divisible by 2 and 3 both.
v1 = int(input("enter any number:"))
if v1%2 == 0 and v1%3 == 0:
    print("yes it is divisible")
else:
    print("no it is not divisible")

# 37.Write a program to accept the age of 4 people and display the youngest one.
age1 = int(input("enter your age:"))
age2 = int(input("enter your age:"))
age3 = int(input("enter your age:"))
age4 = int(input("enter your age:"))
if age1<age2  and age1<age3 and age1< age4:
    print("youngest one is :", age1)
elif age2<age1 and age2<age3 and age2<age4:
    print("youngest one is:", age2)
elif age3<age1 and age3<age2 and age3< age4:
    print("youngest one is:", age3)
else:
    print("youngest one is:", age4)

# 38. Write a program to accept the age of 4 people and display the oldest one.
age1 = int(input("enter your age:"))
age2 = int(input("enter your age:"))
age3 = int(input("enter your age:"))
age4 = int(input("enter your age:"))
if age1>age2  and age1>age3 and age1>age4:
    print("oldest one is :", age1)
elif age2>age1 and age2>age3 and age2>age4:
    print("oldest one is:", age2)
elif age3>age1 and age3>age2 and age3> age4:
    print("oldest one is:", age3)
else:
    print("oldest one is:", age4)

# 39. Write a program to check whether a number is prime or no
num = 5
if num > 1:
	for i in range(2, int(num/2)+1):
		if (num % i) == 0:
			print(num, "is not a prime number")
		break
	else:
		print(num, "is a prime number")