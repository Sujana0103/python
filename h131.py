num=int(input())
l=list(map(int,input().split()))
a=sorted(l)
b=a[::-1]
arr=[]
for i in range(0,len(l)):
  arr.append(b[i])
  arr.append(a[i])
for j in arr[:len(l)]:
  print(j,end=" ")
