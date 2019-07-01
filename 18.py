no1,no2=map(int,input().split())
for num in range(no1+1,no2):
  sum=0
  temp0=num
  while temp0>0:
    digit=temp0%10
    sum+=digit**3
    temp0//=10
  if num==sum:
    print(num,end=' ')
