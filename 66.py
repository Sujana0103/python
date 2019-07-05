num=int(input())
cnt=0
for i in range(2,num):
 if(num%i==0):
  cnt=cnt+1
if(cnt<=0):
 print("yes")
else:
 print("no")
