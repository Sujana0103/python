digit1,digit2=map(int,input().split())
for i in range(digit1+1,digit2):
  if((i%2)==0):
    print(i,end='')
