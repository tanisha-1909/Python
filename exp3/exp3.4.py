p=float(input("enter amount"))
rate=float(input("enter rate"))
time=float(input("enter time"))

amount=p*(1+rate/100) **time
print(amount)
