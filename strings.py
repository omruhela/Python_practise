# Input:
# s = "hello"

# Output:
# "olleh"
'''word=input("Enter the word : ")
rev=""
for i in str(word):
    rev=i+rev
print(rev)'''



# Input:
# s = "madam"

# Output:
# true
'''word=input("Enter the word : ")
rev=""
for i in word:
    rev=i+rev
if(rev==word):
    print("It is a Palindrome..")
else:
    print("It is not a Palindrome....")'''



# Input:
# s = "hello"

# Output:
# 2
'''word=input("Enter the word : ")
count=0
for i in word:
    if (i=='a' or i=='e'  or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' ):
        count+=1
print(count)'''



# Input:
# s = "hello"

# Output:
# 3
'''word = input("Enter the word: ")
count = 0
for i in word:
    if ((i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z')) and \
       not (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or 
            i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count += 1
print("Number of consonants:", count)'''




# Input:
# s = "hello world"

# Output:
# 1
'''word=input("Enter the word : ")
count=0
for i in word:
    if (i==' '):
        count+=1
print(count)'''



# Input:
# s = "banana"
# c = "a"

# Output:
# 3
'''s=input("enter the word : ")
c=input("Enter the letter you want to check it how many times it occured : ")
count=0
for i in s:
    if(i==c):
        count+=1
print(f"The number of times {c} occurred: {count}")'''



# Input:
# s = "a b c"

# Output:
# "abc"
'''s = input("Enter the string: ")
result = ""
for i in s:
    if i != ' ':
        result = result + i
print(result)'''



# Input:
# s = "I love Python"

# Output:
# "Python love I"
'''s=input("Enter the string : ")
result=""
word=""
for i in s + " ":
    if (i!=" "):
        word=word+i
    else:
        result=word + " " + result
        word=""
print(result)'''



# Input:
# s1 = "listen"
# s2 = "silent"

# Output:
# true

'''word1=input("Enter the first  word : ")
word2=input("Enter the  second word : ")
if(len(word1)!=len(word2)):
    print("False")
else:
    flag=1
    for i in word1:
        count1=0
        count2=0
        for j in word1:
            if(i==j):
                count1+=1
        for k in word2:
            if (j==k):
                count2+=1
        if (count1!=count2):
            flag=0
            break
    if flag==1:
        print("True")
    else:
        print("False")'''
