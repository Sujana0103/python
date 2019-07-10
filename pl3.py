strg1,strg2=input().split()
cost=abs(len(strg2)-len(strg1))
for g in range(len(strg1)):
    if(len(strg2)==1 and strg2[g] in strg1):
        break
    if (strg1[g]!=strg2[g]):
        cost=cost+1
print(cost)
