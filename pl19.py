intg=int(input())
arr=[]
brr=[]
for i in range(intg):
    arr.append(list(map(int,input().split())))
for j in arr:
    for k in j:
        brr.append(k)
brr.sort()
for i in brr:
    print(i,end=' ')
