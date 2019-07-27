a1,b2=map(int,input().split())
arr=[]
x=0
for i in range(a1):
    arr.append(list(map(int,input().split())))   
for i in range(a1):
    for j in range(b2-1):
        for k in range(j+1,b2+1):
            if arr[i][j:k]==[1]*len(arr[i][j:k]):
                 if all(arr[p+i][j:k]==[1]*len(arr[p+i][j:k]) for p in range(len(arr[i][j:k])-1)):
                     if len(arr[i][j:k])>x:
                        x=len(arr[i][j:k])
if len(arr)==1 and len(arr[0])==1 and arr[0][0]==1:
    print(1)
for i in range(x):
    print(*[1]*x) 
