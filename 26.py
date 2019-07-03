num=int(input())
a=list(map(int,input().split()[:num]))
a.sort()
for i in a:
  print(i,end=" ")
