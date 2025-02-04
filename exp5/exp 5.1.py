def prime_num(num):
    sum=0

    for i in range(2,num+1):
        for j in range (2,i):
            if(i%j==0):
                break
            else:
                sum=sum+i
    return sum

num=int(input("enter number"))
print("the sum of primes is" ,prime_num(num))