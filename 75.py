strg=list(input())
if len(strg)%2==0:
    strg[int(len(strg)/2)] ='*'
    strg[int(len(strg)/2)-1]='*'
else:
    strg[int(len(strg)/2)] ='*'
for i in range(0,len(strg)):
    print(strg[i],end='')
