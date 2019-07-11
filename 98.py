intg=int(input())
nums=list(map(int,input().split()))
for i in range(len(nums)-1):
   if(nums[i]>nums[i+1]):
      print(i)
