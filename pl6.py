intg=int(input())
nums=list(map(int,input().split()))
o=0
for i in range(0,intg-2):
	for j in range(1,intg-1):
		for k in range(2,intg):
			if(nums[i]<nums[j] and nums[j]<nums[k]):
				o+=1
print(o)
