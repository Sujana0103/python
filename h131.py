intg=int(input())
l=list(map(int,input().split()))
u=sorted(lis1)
v=u[::-1]
arr=[]
for i in range(0,len(l)):
  arr.append(v[i])
  arr.append(u[i])
for j in arr[:len(l)]:
  print(j,end=" ")
