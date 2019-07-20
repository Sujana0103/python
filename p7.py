a1=input()
len=len(a1)
arr=[]
for i in range(0,len,2):
    arr.append(a1[i:i+2][::-1])
print(''.join(arr))
