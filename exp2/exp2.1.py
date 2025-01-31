import math
x1=int(input("enter x value of point 1 "))
y1=int(input("enter y value of point 1"))

x2=int(input("enter x value of point 2"))
y2=int(input("enter x value of point 1"))

temp1=x1-x2
temp1=temp1*temp1

temp2=y1-y2
temp2=temp2*temp2

print("distance is" ,math.sqrt(temp1+temp2))