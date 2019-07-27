intg1,intg2=map(int,input().split())
l=list(map(int,input().split()[:intg1]))
intg1=[]
l.insert(0,0)
for i in range(intg2):
    arr=[]
    lxor=0
    intg3,intg4=map(int,input().split())
    for j in range(intg3,intg4+1):
        lxor^=l[j]
    intg1.append(lxor)
for i in intg1:
	print(i)
