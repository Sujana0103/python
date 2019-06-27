a1,b2,c3=map(int,input().split())
if((a1>b2) and (a1>c3)):
  print(a1)
elif((b2>c3) and (b2>a1)):
  print(b2)
else:
  print(c3)
