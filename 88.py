a1,b2=map(int,input().split())
if(a1>b2):
  great=a1
else:
  great=b2
while(True):
  if((great%a1) == 0 and (great%b2) == 0):
    lcm=great
    break
  great=great+1
print(lcm)
