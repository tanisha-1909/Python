num=50
a=1
b=2
sum=0

while b<50:
    if(b%2==0):
        sum=sum+b  
    a,b=b,a+b
    print(b)
print("the sum of even terms is", sum)