intg1,intg2=map(int,input().split())
l=list(map(int,input().split()[:intg1]))
arr=[]
for i in range(intg2):
	intg3,intg4=list(map(int,input().split()))
	arr.append(min(l[intg3-1:intg4]))
for j in arr:
	print(j)
