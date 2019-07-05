a1,b2=map(int,input().split())
nums=list(map(int,input().split()[:a1]))
rep=0
for i in nums:
   if(i==b2):
      rep=rep+1
print(rep)
