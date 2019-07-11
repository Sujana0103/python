a1,b2=map(str,input().split())
y=0
if len(a1)>len(b2):
	a1,b2=b2,a1
p=0
while p<len(a1):
	  y+=(ord(b2[p])-ord(a1[p]))
	  p+=1
for p in range(p,len(b2)):
	  y+=ord(b2[p])-ord('a')+1
print(y)
