intg=int(input())
n=0
arr=[]
for i in range(1,intg+1):
	arr.append(i)
for i in range(len(arr)):
	for i in range(i+1,len(arr)):
		n+=1
print(n)
