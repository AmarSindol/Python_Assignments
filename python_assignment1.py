'''Write a program to find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200
(both included). The numbers obtained should be printed in a comma separated sequence on a single line '''
# the below is the code for the above question.

for i in range(2000,3200):
    if(i%7==0) and (i%5!=0):
        print(i,end=',')
print("End of the code")

'''Write a program to accept the user's first and last name and then getting them printed in the reverse order with 
space between first name and last name.'''

# 1st method
a= input(" Enter the first name : ")
b= input(" Enter the last name : ")
c = (a+" "+b)
print(c[::-1])

# 2nd method
a= input(" Enter the first name : ")
b= input(" Enter the last name : ")
c = (a+" "+b)
d=reversed(c)
e = ''.join(d)
print(e)

# 3rd method
a= input(" Enter the first name : ")
b= input(" Enter the last name : ")
c = (a+" "+b)
d=''
e=len(c)-1
while e>=0:
    d=d+c[e]
    e=e-1
print(d)

'''Write a python program to find the volume of the sphere with the diameter 12 cms, formula : V=4/3*pie*r(cube)'''
radius = 12
pie = 3.14
Volume = (4.0/3.0)*pie*(radius**3)
print(Volume)

