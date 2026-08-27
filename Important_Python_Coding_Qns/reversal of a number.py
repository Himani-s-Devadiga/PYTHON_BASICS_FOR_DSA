# reversal of a number
num=58392
reverse=0
while num>0:
  digit=num%10
  reverse=reverse*10+digit
  num=num//10
print("The reversal number is",reverse)
