strg1,strg2=list(map(str,input().split()))
count=0
for i in range(0,len(strg2)):
    if(strg1[i]!=strg2[i]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
