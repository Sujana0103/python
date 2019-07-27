intg=input()
chs=map(int,input().split())
arr=[]
for i in chs:
  x=bin(i)
  arr.append(x)
sarr=sorted(arr)
sarr.reverse()
for j in sarr:
  print(int(j,2))
