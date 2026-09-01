N=int(input("enter the number of digits"))
count=0
while N>0:
  count=count+1
  N=N//10

print(count)  

### Note:
Sometimes a variable doesn't directly calculate the answer. It records what happens during the loop.
