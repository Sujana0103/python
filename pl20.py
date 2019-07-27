a1=input().split()
arr=int(a1[1])
b2=input().split()
b2=[int(i) for i in b2]
b2=sorted(b2,reverse=True)
temp=0
count=0
for i in range(0,len(b2)):
  while True:
    if(temp==arr):
      break
    elif(temp>arr):
      count-=1
      temp-=b2[i]
      break
    elif(temp<arr):
      temp+=b2[i]
      count+=1
print(count)
