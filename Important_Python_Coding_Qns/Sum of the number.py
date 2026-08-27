# Sum of the number

num=int(input("Enter the number"))
total =0
while num>0:
     m=num%10
     total=total+m
     num=num//10
print("The sum of the number is",total)
