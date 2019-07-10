num,intg=input().strip().split(" ")
intg=int(intg)
i=0;
while i<len(num)-1 and intg:
	if(num[i]>num[i+1]):
		intg-=1
		num=num[:i]+num[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
sol=num[:len(num)-intg]
print(sol)
