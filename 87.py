a1,b2=map(int,input().split())
if(a1>b2):
  small=b2
else:
  small=a1
for i in range(1,small+1):
  if(a1%i == 0 and b2%i == 0):
    hcf=i    
print(hcf)
