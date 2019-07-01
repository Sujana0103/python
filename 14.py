number1,number2=map(int,input().split())
for i in range(number1+1,number2):
  if((i%2)!=0):
    print(i,end='')
