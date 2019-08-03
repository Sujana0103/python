intg=int(input())
dig=list(map(int,input().split()))
ans=int(intg/2)
arr=dig[:ans]
brr=dig[ans::]
if ((sum(arr)//len(arr))==(sum(brr)//len(brr))):
    print("yes")
else:
    print("no")
