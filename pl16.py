intg=int(input())
l=list(map(int,input().split()))
arr=[1]*intg
for i in range(intg):
    if i==0:
        if l[i]>l[i+1]:
            arr[i]=arr[i]+arr[i+1]
    elif i>0:
        if l[i]>l[i-1]:
            arr[i]=arr[i]+arr[i-1]
print(sum(arr))
