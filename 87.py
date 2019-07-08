a1,b2=map(int,input().split())
if(a1>b2):
  small=b2
else:
  small=b1
for i in range(2,small+1):
  if(a1%i == 0 and b2%i == 0):
    print(i)
