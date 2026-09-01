N=int(input("Enter the numbers to be counted"))
count=0
i=1
while i<=N:
      if i%3==0:
          count=count+1
      i=i+1
  
print(count)
