n1,k2=map(int,input().split())
intg=list(map(int,input().split()[:k2]))
a=[]
for i in intg:
   if(i<=i+1):
     a.append(i)
print(a[k2-1]) 
