'''Write a program to print half diamond using nested for loop'''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print('*',end=' ')
    print()

'''Write a program to reverse a word after accepting from the user'''
# 1st method
n=input("Enter the string : ")
print(n[::-1])

#2nd method
n=input("Enter the string : ")
s=reversed(n)
print(''.join(s))

#3rd method
n=input('Enter the String : ')
s=''
a=len(n)-1
while a>=0:
    s=s+n[a]
    a=a-1
print(s)