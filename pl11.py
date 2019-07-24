a=int(input())
x=0
arr=[]
for i in range(1,a+1):
	arr.append(i)
for i in range(len(arr)):
	for i in range(i+1,len(arr)):
		x+=1
print(x)
