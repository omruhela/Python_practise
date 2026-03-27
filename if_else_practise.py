#Practising the operator questions 

# Take a 3-digit number and find sum of digits using % and //.
'''num=int(input("Enter the number : "))
digit_1=num//100
digit_2=(num//10)%10
digit_3=num%10
final=digit_1+digit_2+digit_3
print(final)'''

# Take two numbers and print remainder without using % (use formula).
'''a = int(input("Enter first number (dividend): "))
b = int(input("Enter second number (divisor): "))

quotient = a // b
remainder = a - (b * quotient)

print("Remainder:", remainder)'''

# Take a number and print half of it\
'''num=int(input("Enter the number : "))
half_num=num/2
print("The half of the number is : ",half_num)'''

# Take two numbers and swap them using arithmetic operators
'''a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
a=a+b
b=a-b
a=a-b
print("Value of a after swapping : ",a)
print("Value of b after swapping : ",b)'''


#Take total seconds and convert into minutes (use // and %)
'''total_sec=int(input("Enter the time in seconds : "))
min=total_sec//60
sec=total_sec%60
print("the total minutes is : ", min,"minutes",sec,"seconds")'''


# Take temperature in Celsius and convert to Fahrenheit.
'''temp=float(input("Enter the temperature in celcius : "))
f=(temp*9/5)+32
print("The temperature in fahrenheit is : ",f)'''


#Take total bill and number of people, calculate per person share.\
'''bill=float(input("Enter the Total bill : "))
num_of_person=int(input("Enter the number of persons :  "))
share_per_person=bill/num_of_person
print("The share per person is : ",share_per_person)'''

#BASIC LEVEL CONDITONALS------------------------------------        

#Take age and check if age is greater than 18.
'''age=int(input("Enter the age : "))
if(age>18):
    print("Age is greater than 18 ")
else:
    print("Age is lesser than 18 ")'''


#Take a number and check if it is positive, negative, or zero.
'''num=int(input("Enter the number : "))
if(num>0):
    print("Postive ")
elif(num==0):
    print("Zero")
elif(num<0):
    print("Negative")
else:
    print("Invalid input")    '''


# Take a number and check if it is even or odd.
'''num=int(input("Enter the number you want to check : "))
if(num%2):
    print("Number is even")
else:
    print("Number is odd")'''

# 3. Take age and print:
#     - "Child" if age < 13
#     - "Teen" if age 13–19
#     - "Adult" otherwise
'''age=int(input("Enter the age : "))
if(age<13):
    print("Child")
elif(age>13 and age<19):
    print("Teen")
else:
    print("Adult")'''

#4. Take marks and print:
# - "Fail" if < 35
# - "Pass" if 35–59
# - "First Class" if 60–79
# - "Distinction" if 80+
'''marks=int(input("Enter the marks : "))
if(marks<35):
    print("Fail")
elif(marks>35 and marks<39):
    print("Pass")
elif(marks>60 and marks<79):
    print("First")
elif(marks>80):
    print("Distinction")'''


# 5. Take temperature and print:
#     - "Cold" if < 15
#     - "Warm" if 15–30
#     - "Hot" if > 30
'''temp=int(input("Enter the temperature : "))
if(temp<15):
    print("Cold")
elif(temp>15 and temp<30):
    print("Warm")
elif(temp>30):
    print("Hot")
else:
    print("Invalid input")'''


# Take a number and check if it is divisible by 3, 5, or both.
'''num=int(input("Enter the number : "))
if(num%3==0 and num%5==0):
    print("The number is divisible by both 3 and 5")
elif(num%3==0):
    print("The number is divisible by 3")
elif(num%5==0):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 3 and 5 ")'''


# Take two numbers and print which one is greater or if equal.
'''num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
if(num1>num2):
    print("The first number is greater ")
elif(num1<num2):
    print("The second number is greater ")
elif(num1==num2):
    print("The both the numbers are equal ")'''

# Take a character and check if it is a vowel or consonant.
'''ch=input("Enter the character : ")
if(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U') or (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("Vowel")
else:
    print("Consonant")'''

#Take a year and check if it is leap year or not.
'''year=int(input("Enter the year : "))
if(year%4==0 and year%11!=0) or (year%400==0):
    print("This is a leap year ")
else:
    print("This is not a leap year ")'''

#Take a number and check if it is 1-digit, 2-digit, or 3-digit.
'''num = int(input("Enter a number: "))
if num >= 0 and num <= 9:
    print("1-digit number")
elif num >= 10 and num <= 99:
    print("2-digit number")
elif num >= 100 and num <= 999:
    print("3-digit number")
else:
    print("Number is more than 3 digits")'''

#14. Take username and check:
    # - "admin" → Admin Access
    # - "guest" → Guest Access
    # - otherwise → Invalid User
'''username = input("Enter username: ")
if username == "admin":
    print("Admin Access")
elif username == "guest":
    print("Guest Access")
else:
    print("Invalid User")'''

#Take password and check if it matches "python123".
'''password = input("Enter password: ")
if password == "python123":
    print("Access Granted")
else:
    print("Incorrect Password")'''

#Take three numbers and print the largest.
'''a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if(a>b and a>c):
    print("The largest number is a  ")
elif(b>a and b>c):
    print("The largest number is b ")
elif(c>a and c>b):
    print("The largest number is c")'''

#1. Take a number and print:
    # - "Fizz" if divisible by 3
    # - "Buzz" if divisible by 5
    # - "FizzBuzz" if divisible by both
    # - otherwise print number
'''num=int(input("Enter the number : "))
if(num%3==0):
    print("Fizz")
elif(num%5==0):
    print("Buzz")
elif(num%3==0 and num%5==0):
    print("FizzBuzz")
else:
    print(" the number you entered : ",num)'''


#Take a number and check Armstrong number (3-digit
'''num = int(input("Enter a 3-digit number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
if num == (a**3 + b**3 + c**3):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")'''


#Take product price and customer type (regular/premium) and calculate discount.
'''price = float(input("Enter product price: "))
customer = input("Enter customer type (regular/premium): ")
if customer.lower() == "regular":
    discount = price * 0.10   # 10% discount
elif customer.lower() == "premium":
    discount = price * 0.20   # 20% discount
else:
    discount = 0
    print("Invalid customer type")
final_price = price - discount
print("Discount:", discount)
print("Final Price:", final_price)'''


