# Given an integer N, print numbers from 1 to N using a for loop.
'''N=int(input("Enter the number:  " ))
for i in range(N+1):
    print(i)'''


# Numbers from 1 to N (space separated).
'''num=int(input("Enter the number : "))
for i in range(1,num+1):
    print(i,end=" ")'''


# Given N, compute the sum of numbers from 1 to N.
'''N=int(input("Enter the number : "))
sum=0
for i in range(1,N+1):
    sum+=i
print(sum)'''



# Given an integer N, print its multiplication table up to 10.
'''N=int(input("Enter the number : "))
for i in range(1,10+1):
    print(N,"X",i,"=",N*i)'''


# Given N, count how many even numbers exist between 1 and N
'''N=int(input("Enter the number :"))
count=0
for i in range(1,N+1):
    if(i%2==0):
        count+=1
print(count)'''


# Print squares of numbers from 1 to N.
'''n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(i**2, end=" ")'''


# Given an integer N, count how many digits it contains.
'''n=int(input("enter the number : "))
count=0
for i in str(n):
    count+=1
print(count)'''


# Given N, find sum of its digits.
'''n=int(input("Enter the number : "))
sum=0
for i in str(n):
    sum+=int(i)
print(sum)'''


# Given a string S, count number of vowels.
'''name=input("Enter the string : ")
count=0
for i in name:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(count)'''


# Compute factorial of N using loop
'''n=int(input("Enter the number : "))
f=1
for i in range(1,n+1):
    f*=i
print(f)'''

# Reverse digits of integer N.
'''n=input("enter the number : ")
rev=''
for i in str(n):
    rev=i+rev
print(rev)'''


# Print first N Fibonacci numbers.
'''n=int(input("enter the number : "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c'''


# Determine if N is prime.
'''n=int(input("enter the number : "))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("prime ")
else:
    print("not prime")   '''


# 1. Pattern – Number Triangle
# Input: 4
# Output:
# 1
# 12
# 123
# 1234

'''n = int(input("Enter the number: "))
for i in range(n + 1):
    for j in range(i + 1):
        print(i, end="")
    print()'''

# Given an integer N, print a centered pyramid of stars.
# *
# **
# ***
# ****
# *****
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''


# *****
# ****
# ***
# **
# *
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()'''

#      *
#     **
#    ***
#   ****
#  *****
# ******
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''


#    *
#   ***
#  *****
# *******
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for i in range(i+1):
        print("*",end=" ")
    for i in range(i):
        print("*",end=" ")
    print()'''


# *******
#  *****
#   ***
#    *
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()'''

#    1
#   121
#  12321
# 1234321
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()'''


#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
'''n=int(input("Enter the number : "))
for i in range(n-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i-1):
        print("*",end="")
    for j in range(n-i):
        print("*",end="")
    print()'''

# *    *
# *    *
# *    *
# *    *
# *    *
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#         * 
#         * 
#     * * * * *
#         * 
#         * 
'''n=int(input("Enter the nuumber : "))
for i in range(n):
    for j in range(n):
        if(i==n//2 or j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


#     * * * * * 
#     *       *
#     *       *
#     *       *
#     * * * * *    
'''n=int(input("Enter the number : "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


