n, k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
if k == 0:
  print(0)
if k == len(nums):
  print(nums[k - 1])
else:
  if nums[k] == nums[k - 1]:
    print(-1)
  else:
    print(nums[k-1])
  
