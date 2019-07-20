a1=int(input())
sum=0
b2=input().split()
for i in range(len(b2)):
  x=int(b2[i])
  for j in range(i):
      if(int(b2[j])<x):
        sum=sum+int(b2[j])

print(sum)
